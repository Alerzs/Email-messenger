
#admin email:admin    admin password:1234

import pickle
import hashlib
class Manage:

    def __init__(self) -> None:
        with open('data.pkl', 'rb') as inp:
            data = pickle.load(inp)
        inp.close()
        self.users_list = data
        


    def save(self):
        with open('data.pkl', 'wb') as otp:
            pickle.dump(self.users_list , otp)

    def creat_hash(self,password):
        enc = password.encode()
        sha256 = hashlib.sha256(enc)
        string_hash = sha256.hexdigest()
        return string_hash
    
    def admin_check(self ,user):
        if user.email == "admin" and user.password == self.creat_hash("1234"):
            return True
        return False

    def add_new_member(self,email,password):
        self.users_list.append(User(email ,password))

    def change_password(self ,user ,new_password):

        for idx , person in enumerate(self.users_list):
            if person == user:
                changing_user = self.users_list.pop(idx)
                changing_user.password = self.creat_hash(new_password)
                self.users_list.append(changing_user)

    def validation(self ,email ,password) -> bool:
        for user in self.users_list:
            if user.email == email and user.password == self.creat_hash(password):
                return user
        return False
    
    def send_email(self ,sender_email ,reciver_email ,text):
        self.find_user(reciver_email).inbox.append(f"{sender_email} : {text}")

    def find_user(self, email):
        for user in self.users_list:
            if user.email == email:
                return user
        return False


class User:

    def __init__(self ,email ,password ) -> None:
        self.email = email
        self.password = self.creat_hash(password)
        self.inbox = []

    def creat_hash(self,password):
        enc = password.encode()
        sha256 = hashlib.sha256(enc)
        string_hash = sha256.hexdigest()
        return string_hash

    def inbox_print(self):
        print(self.inbox)
        

while True:
    print("welecome to email messenger")
    email = input("please enter your email address : ")
    password = input("please enter your password : ")
    manage = Manage()
    current_user = manage.validation(email ,password)
    if current_user is not False:
        admin_check = manage.admin_check(current_user)
        while True:
            if admin_check :
                print("press 'A' to add new member")
            try:
                print("press 'S' to send email")
                print("press 'I' to see your inbox")
                print("press 'C' to change your password")
                print("press 'E' to exit")
                inp = input().upper()
            except:
                print("!!! entered option is wrong !!!")
                continue
            if inp == "S":
                target = manage.find_user(input("please enter reciver email : "))
                if target == False:
                    print("User not found")
                    continue
                text = input("please write your massege : ")
                manage.send_email(current_user.email ,target.email , text)
                
            elif inp == "I":
                current_user.inbox_print()

            elif inp == "A" and admin_check :
                member_email = input("please enter new members email")
                member_password = input("please enter new members password")
                manage.add_new_member(member_email ,member_password)

            elif inp == "C":
                new_pass = input("please enter your new password")
                manage.change_password(current_user , new_pass)
            elif inp == "E":
                manage.save()
                exit()
            else:
                print("wrong option")
    else:
        print("user not found")



