import uuid
from datetime import datetime

class User:
    def __init__(self, id=None, username="", email="", password=""):
        self.id = str(uuid.uuid4()) if id is None else id
        self.username = username
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the User object"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }

    def __str__(self):
        """Returns a string representation of the User object"""
        return f"User({self.id}, {self.username}, {self.email})"

