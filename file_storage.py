import json
import os

class FileStorage:
    """Class for storing and retrieving data"""
    __file_path = "lolo_cookies.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Reloads the stored objects from the JSON file"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            for k, v in obj_dict.items():
                cls_name = v["__class__"]
                cls = self.classes()[cls_name]
                FileStorage.__objects[k] = cls(**v)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.cookie import Cookie
        from models.user import User
        from models.order import Order

        classes = {"Cookie": Cookie, "User": User, "Order": Order}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for each class"""
        attributes = {
            "Cookie": {"id": str, "name": str, "price": float},
            "User": {"id": str, "username": str, "email": str, "password": str},
            "Order": {"id": str, "user_id": str, "cookie_id": str, "quantity": int, "total_price": float}
        }
        return attributes

