import uuid
from datetime import datetime

class Order:
    def __init__(self, id=None, user_id="", cookie_id="", quantity=1, total_price=0.0):
        self.id = str(uuid.uuid4()) if id is None else id
        self.user_id = user_id
        self.cookie_id = cookie_id
        self.quantity = quantity
        self.total_price = total_price
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the Order object"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "cookie_id": self.cookie_id,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }

    def __str__(self):
        """Returns a string representation of the Order object"""
        return f"Order({self.id}, User: {self.user_id}, Cookie: {self.cookie_id}, Quantity: {self.quantity}, Total: {self.total_price})"
    def send_whatsapp_message(to, body):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=body,
        to=f'whatsapp:{to}'
        )
        return message.sid
    def create_order(user, cookie_id, quantity):
    # Create the order
    order = Order(user_id=user.id, cookie_id=cookie_id, quantity=quantity, total_price=calculate_price(cookie_id, quantity))
    storage.new(order)
    storage.save()

    # Prepare the order details
    order_details = f"Hello {user.username},\n\nYour order has been placed successfully!\n\nOrder ID: {order.id}\nCookie: {cookie_id}\nQuantity: {quantity}\nTotal Price: ${order.total_price:.2f}\n\nThank you for ordering from Lolo Cookies!"

    # Send order details via WhatsApp
    send_whatsapp_message(user.phone_number, order_details)

    return order


