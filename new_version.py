
#admin email:admin    admin password:1234

import pickle
import hashlib
from os import system
clear = lambda :system("cls")

class Manage:

    def __init__(self) -> None:
        with open('user_data.pkl', 'rb') as inp:
            data = pickle.load(inp)
        inp.close()
        self.users_list = data
        

    def save(self):
        with open('user_data.pkl', 'wb') as otp:
            pickle.dump(self.users_list , otp)


    @staticmethod
    def __creat_hash(password):
        enc = password.encode()
        sha256 = hashlib.sha256(enc)
        string_hash = sha256.hexdigest()
        return string_hash
    

    def add_new_member(self,email,password):
        self.users_list.append(User(email ,password))


    def validation(self ,email ,password) -> bool:
        hashword = self.__creat_hash(password)
        for user in self.users_list:
            if user.get_email() == email and user.get_password() == hashword:
                return user
        return False
    

    def send_email(self ,sender ,reciver_email ,text):
        reciver = self.__find_user(reciver_email)
        if reciver == False:
            print("email not found")
            return
        reciver.get_inbox().append(f"{sender.get_email()} : {text}")
        print("sent successfully")


    def __find_user(self, email):
        for user in self.users_list:
            if user.get_email() == email:
                return user
        return False


class User:

    def __init__(self ,email ,password ) -> None:
        self.__email = email
        self.__password = self.__creat_hash(password)
        self.__inbox = []


    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_inbox(self):
        return self.__inbox


    @staticmethod
    def __creat_hash(password):
        enc = password.encode()
        sha256 = hashlib.sha256(enc)
        string_hash = sha256.hexdigest()
        return string_hash


    def inbox_print(self):
        if len(self.__inbox) == 0:
            print("your inbox is empty")
        else:
            for mail in self.__inbox:
                print(mail)
        

    def admin_check(self):
        if self.__email == "admin" and self.__password == self.__creat_hash("1234"):
            return True
        return False


    def change_password(self ,new_password):
        self.__password = self.__creat_hash(new_password)


while True:
    print("welecome to email messenger")
    email = input("please enter your email address : ")
    password = input("please enter your password : ")
    manage = Manage()
    current_user = manage.validation(email ,password)

    if current_user is not False:
        admin_check = current_user.admin_check()

        while True:
            clear()
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
                clear()
                target_email = input("please enter reciver email : ")
                text = input("please write your massege : ")
                manage.send_email(current_user ,target_email , text)
                input("press enter to continue")
                
            elif inp == "I":
                clear()
                current_user.inbox_print()
                input("press enter to continue")

            elif inp == "A" and admin_check :
                clear()
                member_email = input("please enter new members email : ")
                member_password = input("please enter new members password : ")
                manage.add_new_member(member_email ,member_password)

            elif inp == "C":
                clear()
                new_pass = input("please enter your new password : ")
                current_user.change_password(new_pass)
            elif inp == "E":
                manage.save()
                exit()
            else:
                print("wrong option")
    else:
        print("user not found")




