class Manage:

    def __init__(self) -> None:
       #open stored hash data file
        pass 
    

    def creat_hash(self):
        #use to convert user object to hash
        pass
    
    def admin_check(self ,user):
        #checks if given user is admin or not
        pass

    def add_new_member(self,email,password):
        #add a member to hash file shold use creat_hash function in it
        #this method is called by admin to add a new member
        pass

    def change_password(self ,user ,new_password):
        pass

    def validation(self ,email ,password) -> bool:
        # checks if data already has a member with given email and password and returns user object if its valid otherwise returns false
        pass
    
    def send_email(self ,sender_email ,reciver_email ,text):
        pass

    def find_user(self, email):
        pass

class User:

    def __init__(self ,email ,password ,inbox) -> None:
        self.email = email
        self.password = password
        self.inbox = []

    

    def inbox_print(self):
        pass
        

    




while True:
    print("welecome to email messenger")
    email = input("please enter your email address : ")
    password = input("please enter your password : ")
    manage = Manage()
    current_user = manage.validation(email ,password)
    if current_user == User:
        admin_check = manage.admin_check(current_user)
        if admin_check :
            print("press 'A' to add new member")
        while True:
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
                exit()
            else:
                print("wrong option")
    else:
        print("user not found")

