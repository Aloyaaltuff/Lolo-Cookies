import uuid
from datetime import datetime

class Cookie:
    def __init__(self, id=None, name="", price=0.0):
        self.id = str(uuid.uuid4()) if id is None else id
        self.name = name
        self.price = price
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the Cookie object"""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }

