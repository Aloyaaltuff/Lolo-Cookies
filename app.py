from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from basemode import add_user, authenticate
import json
from models.user import User
from models.order import Order
from file_storage import FileStorage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'alo0987667890'
storage = FileStorage()
storage.reload()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    def __repr__(self):
        return f'<User {self.username}>'
        # Create the database and tables
    with app.app_context():
    db.create_all()

def load_users():
    """Load users from a JSON file."""
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    """Save users to a JSON file."""
    with open('users.json', 'w') as f:
        json.dump(users, f)
class Cookie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Cookie {self.name}>'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different username.', 'error')
            return redirect(url_for('register'))

        # Hash the password and add new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Authenticate the user
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('order'))

        else:
            flash('Invalid username or password. Please try again.', 'error')
    if user_is_authenticated:
        return redirect(url_for('order'))
        else:
            return "Invalid credentials", 401

    return render_template('login.html')
@app.route('/order')
def order_page():
    return render_template('order.html')

@app.route('/menu')
def menu():
    cookies = Cookie.query.all()  # Fetch all cookies from the database
    return render_template('products.html', cookies=cookies)

@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        # Extract form data
        cookie_id = request.form['cookie_id']
        quantity = int(request.form['quantity'])
        phone_number = request.form['phone_number']

        # Check if the phone number is provided
        if not phone_number:
            return jsonify({"success": False, "error": "Phone number is required!"}), 400

        # Create a new user or find existing one (for simplicity, assume the user is new)
        user = User(username="guest", email="guest@example.com", phone_number=phone_number)
        storage.new(user)
        storage.save()

        # Create the order
        order = create_order(user, cookie_id, quantity)
        
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def create_order(user, cookie_id, quantity):
    total_price = calculate_price(cookie_id, quantity)
    order = Order(user_id=user.id, cookie_id=cookie_id, quantity=quantity, total_price=total_price)
    storage.new(order)
    storage.save()

    order_details = (
        f"Hello {user.username},\n\n"
        f"Your order has been placed successfully!\n\n"
        f"Order ID: {order.id}\n"
        f"Cookie: {cookie_id}\n"
        f"Quantity: {quantity}\n"
        f"Total Price: ${order.total_price:.2f}\n\n"
        "Thank you for ordering from Lolo Cookies!"
    )

    # Send the order details via WhatsApp
    send_whatsapp_message(user.phone_number, order_details)

    return order

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
