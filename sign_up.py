from datetime import datetime
from random import randint
from hashlib import sha256
from file_Handler import FileHandler
import logging
# import sys
# import msvcrt

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="a",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


class Sign_up:
    student = False
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = self.hashible(password)
        if Sign_up.student == True:
            self.student_code = self.creat_student_code()

    def __str__(self):
        return f'{self.user_name}{self.password}{self.student_code}'

    def creat_student_code(self):
        t = datetime.now().year
        w = []
        w.append(str(t)[2:4])
        for i in range(8):
            s = randint(0, 9)
            w.append(str(s))
        self.student_code = ''.join(w)
        return self.student_code

    @staticmethod
    def hashible(a):
        hashed = sha256(a.encode()).hexdigest()
        return hashed


def registeration():
    select = True
    while select:
        print(''' Register as:
                  1-Responsible for Training
                  2-Student
                    ''')
        choice = input('enter your choice: ')
        if choice == "1":
            username = input("Enter Your User Name: ").lower().replace(" ", "")
            reader = FileHandler("List_of_Staff.csv")
            result = reader.read_file()
            for i in result:
                while i["UserName"] == username :
                    logging.info(f'{username} exists')
                    print(''''
                            this username exist,
                            please choose another username''')
                    username = input("Enter Your User Name: ").lower().replace(" ", "")

            password_1 = input("Enter Your Password: ")
            password_2 = input("Enter Your Password again: ")
            while password_1 != password_2:
                logging.warning(f'your password is wrong ')
                password_1 = input("Enter Your Password: ")
                password_2 = input("Enter Your Password again: ")
            else:
                ins = Sign_up(username, password_1)
                logging.info(f'{username} is Registered as Responsible for Training')
                print("You Are Registered as Responsible for Training")
                new_reg = {"UserName": ins.user_name, "Password": ins.password}
                path = FileHandler("List_of_Staff.csv")
                path.add_to_file(new_reg)
                select = False
        elif choice == "2":
            Sign_up.student = True
            username = input("Enter Your User Name: ").lower().replace(" ", "")
            reader = FileHandler("List_of_Student.csv")
            result = reader.read_file()
            for i in result:
                while i["UserName"] == username:
                    logging.info(f'{username} exists')
                    print(''''
                            this username exist,
                            please choose another username''')
                    username = input("Enter Your User Name: ").lower().replace(" ", "")

            password_1 = input("Enter Your Password: ")
            password_2 = input("Enter Your Password again: ")
            while password_1 != password_2:
                logging.warning(f'your password is wrong ')
                password_1 = input("Enter Your Password: ")
                password_2 = input("Enter Your Password again: ")
            else:
                ins = Sign_up(username, password_1)
                logging.info(f'{username} is Registered as student')
                print("You Are Registered as Student")
                file_2 = {"UserName": ins.user_name, "Password": ins.password, "StudentId": ins.student_code}
                path_2 = FileHandler("List_of_Student.csv")
                path_2.add_to_file(file_2)
                select = False
        else:
            select = False
