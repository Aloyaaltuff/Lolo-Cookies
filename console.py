#!/usr/bin/env python3

import argparse
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
from basemode import authenticate
from models.user import User
from app import db  # Import the database instance

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

def register_user(username, password):
    """Register a new user."""
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        print("Username already exists. Please choose a different username.")
        return False

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    print(f"User '{username}' registered successfully.")
    return True

def login_user(username, password):
    """Login a user."""
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        print(f"Login successful! Welcome, {username}.")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def main():
    """Main function to parse arguments and route commands."""
    parser = argparse.ArgumentParser(description='Lolo Cookies Command Line Interface')
    subparsers = parser.add_subparsers(dest='command')

    # Register command
    register_parser = subparsers.add_parser('register', help='Register a new user')
    register_parser.add_argument('username', type=str, help='Username for registration')
    register_parser.add_argument('password', type=str, help='Password for registration')
    register_parser.set_defaults(func=register_user)

    # Login command
    login_parser = subparsers.add_parser('login', help='Log in a user')
    login_parser.add_argument('username', type=str, help='Username for login')
    login_parser.add_argument('password', type=str, help='Password for login')
    login_parser.set_defaults(func=login_user)

    args = parser.parse_args()

    if args.command:
        if args.command == 'register':
            success = args.func(args.username, args.password)
            if not success:
                print("Registration failed.")
        elif args.command == 'login':
            args.func(args.username, args.password)
        else:
            parser.print_help()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
