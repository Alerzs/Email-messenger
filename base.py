import hashlib
import json
import os

class Manage:

    def __init__(self) -> None:
        self.load_data()

    def load_data(self):
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                self.users = json.load(f)
        else:
            self.users = {}

    def save_data(self):
        with open("users.json", "w") as f:
            json.dump(self.users, f)

    def create_hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def admin_check(self, user):
        return user.get("is_admin", False)

    def add_new_member(self, email, password, is_admin=False):
        if email in self.users:
            print("User already exists.")
            return
        self.users[email] = {
            "password": self.create_hash(password),
            "inbox": [],
            "is_admin": is_admin
        }
        self.save_data()
        print(f"User {email} added successfully.")

    def change_password(self, user_email, new_password):
        self.users[user_email]["password"] = self.create_hash(new_password)
        self.save_data()
        print("Password changed successfully.")

    def validation(self, email, password) -> bool:
        if email in self.users and self.users[email]["password"] == self.create_hash(password):
            return self.users[email]
        return False

    def send_email(self, sender_email, receiver_email, text):
        if receiver_email not in self.users:
            print("Receiver not found.")
            return
        email = {
            "sender": sender_email,
            "text": text
        }
        self.users[receiver_email]["inbox"].append(email)
        self.save_data()
        print("Email sent successfully.")

    def find_user(self, email):
        if email in self.users:
            return self.users[email]
        return None

class User:

    def __init__(self, email, user_data) -> None:
        self.email = email
        self.password = user_data["password"]
        self.inbox = user_data["inbox"]
        self.is_admin = user_data.get("is_admin", False)

    def inbox_print(self):
        for email in self.inbox:
            print(f"From: {email['sender']}, Message: {email['text']}")


while True:
    print("Welcome to Email Messenger")
    email = input("Please enter your email address: ")
    password = input("Please enter your password: ")
    manage = Manage()
    user_data = manage.validation(email, password)
    
    if user_data:
        current_user = User(email, user_data)
        admin_check = manage.admin_check(user_data)
        
        if admin_check:
            print("Press 'A' to add new member")
        
        while True:
            try:
                print("Press 'S' to send email")
                print("Press 'I' to see your inbox")
                print("Press 'C' to change your password")
                print("Press 'E' to exit")
                inp = input().upper()
            except Exception as e:
                print("!!! Entered option is wrong !!!")
                print(e)
                continue

            if inp == "S":
                target_email = input("Please enter receiver email: ")
                target = manage.find_user(target_email)
                if target:
                    text = input("Please write your message: ")
                    manage.send_email(current_user.email, target_email, text)
                else:
                    print("Receiver not found.")
                
            elif inp == "I":
                current_user.inbox_print()

            elif inp == "A" and admin_check:
                member_email = input("Please enter new member's email: ")
                member_password = input("Please enter new member's password: ")
                manage.add_new_member(member_email, member_password)

            elif inp == "C":
                new_pass = input("Please enter your new password: ")
                manage.change_password(current_user.email, new_pass)

            elif inp == "E":
                exit()

            else:
                
                print("Wrong option")
    else:
        print("User not found")
