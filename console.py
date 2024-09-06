#!/usr/bin/env python3

import argparse
import json
import os
import getpass
from basemode import register_user, login_user

COOKIES_FILE = 'cookies.json'

def load_cookies():
    """Load cookies from a JSON file."""
    if os.path.exists(COOKIES_FILE):
        with open(COOKIES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_cookies(cookies):
    """Save cookies to a JSON file."""
    with open(COOKIES_FILE, 'w') as f:
        json.dump(cookies, f, indent=4)

def add_cookie(args):
    """Add a new cookie."""
    cookies = load_cookies()
    if args.cookie not in cookies:
        cookies.append(args.cookie)
        save_cookies(cookies)
        print(f'Added new cookie: {args.cookie}')
    else:
        print(f'Cookie "{args.cookie}" already exists.')

def delete_cookie(args):
    """Delete a cookie."""
    cookies = load_cookies()
    if args.cookie in cookies:
        cookies.remove(args.cookie)
        save_cookies(cookies)
        print(f'Deleted cookie: {args.cookie}')
    else:
        print(f'Cookie "{args.cookie}" not found.')

def list_cookies(args):
    """List all cookies."""
    cookies = load_cookies()
    if cookies:
        print('Cookies:')
        for cookie in cookies:
            print(f'- {cookie}')
    else:
        print('No cookies found.')

def main():
    """Main function to parse arguments and route commands."""
    parser = argparse.ArgumentParser(description='Lolo Cookies Command Interpreter')
    subparsers = parser.add_subparsers(dest='command')

    # Authentication commands
    auth_parser = subparsers.add_parser('auth', help='Authentication commands')
    auth_subparsers = auth_parser.add_subparsers(dest='auth_command')

    # Register command
    register_parser = auth_subparsers.add_parser('register', help='Register a new user')
    register_parser.set_defaults(func=register_user)

    # Login command
    login_parser = auth_subparsers.add_parser('login', help='Log in a user')
    login_parser.set_defaults(func=login_user)

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new cookie')
    add_parser.add_argument('cookie', type=str, help='Name of the cookie to add')
    add_parser.set_defaults(func=add_cookie)

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a cookie')
    delete_parser.add_argument('cookie', type=str, help='Name of the cookie to delete')
    delete_parser.set_defaults(func=delete_cookie)

    # List command
    list_parser = subparsers.add_parser('list', help='List all cookies')
    list_parser.set_defaults(func=list_cookies)

    args = parser.parse_args()

    if args.command == 'auth' and args.auth_command:
        args.func()
    elif args.command:
        if login_user():
            args.func(args)
        else:
            print('Authentication required.')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
