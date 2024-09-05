import json
import os
from hash_password import hash_password

USERS_FILE = 'users.json'

def load_users():
    """Load users from a JSON file."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to a JSON file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def add_user(username, password):
    """Add a new user with hashed password."""
    users = load_users()
    if username in users:
        print(f'User "{username}" already exists.')
    else:
        hashed_password = hash_password(password)
        users[username] = hashed_password
        save_users(users)
        print(f'User "{username}" added.')

if __name__ == "__main__":
    username = input('Enter username: ')
    password = input('Enter password: ')
    add_user(username, password)