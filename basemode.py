import json
import bcrypt

# Path to the JSON file where user data is stored
USER_FILE = 'users.json'

def load_users():
    """Load users from the JSON file."""
    try:
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    """Save users to the JSON file."""
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

def add_user(username, password):
    """Add a new user with hashed password."""
    users = load_users()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users[username] = hashed_password
    save_users(users)

def authenticate(username, password):
    """Authenticate a user."""
    users = load_users()
    hashed_password = users.get(username)
    if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        return True
    return False
