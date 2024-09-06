import bcrypt
import json
import os

USERS_FILE = 'users.json'

def load_users():
    """Load users from a JSON file."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def authenticate(username, password):
    """Authenticate a user with hashed password."""
    users = load_users()
    hashed_password = users.get(username)
    if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        return True
    return False

if __name__ == "__main__":
    username = input('Enter username: ')
    password = input('Enter password: ')
    if authenticate(username, password):
        print('Login successful.')
    else:
        print('Invalid username or password.')
