from datetime import datetime
from random import randint
from hashlib import sha256
from file_Handler import FileHandler
import logging
import os
import pwinput

import sys

# import msvcrt

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="a",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


class Sign_up:
    student = False

    def __init__(self, first_name, last_name, user_name, password):
        self.fname = first_name
        self.lname = last_name
        self.user_name = user_name
        self.password = self.hashible(password)
        if Sign_up.student == True:
            self.student_code = self.creat_student_code()
        else:
            self.student_code = None

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
                  3-Professor
                    ''')
        choice = input('enter your choice: ')
        if choice == "1" or choice == "3":
            Sign_up.student = False
            first_name = input("Enter Your First Name: ").lower().replace(" ", "")
            last_name = input("Enter Your Last Name: ").lower().replace(" ", "")
            username = input("Enter Your User Name: ").lower().replace(" ", "")
            if choice == "1" and os.path.isfile("List_of_Staff.csv"):
                reader = FileHandler("List_of_Staff.csv")
                result = reader.read_file()
                for i in result:
                    while i["UserName"] == username:
                        logging.info(f'{username} exists')
                        print(''''
                                This Username Exist,
                                Please Choose another Username''')
                        username = input("Enter Your User Name: ").lower().replace(" ", "")
            elif choice == "3" and os.path.isfile("List_of_Professor.csv"):
                reader = FileHandler("List_of_Professor.csv")
                result = reader.read_file()
                for i in result:
                    while i["UserName"] == username:
                        logging.info(f'{username} exists')
                        print(''''
                                This Username Exist,
                                Please Choose another Username''')
                        username = input("Enter Your User Name: ").lower().replace(" ", "")


            password_1 = input("Enter Your Password: ")
            password_2 = input("Enter Your Password again: ")
            while password_1 != password_2:
                logging.warning(f'your password is wrong ')
                password_1 = input("Enter Your Password: ")
                password_2 = input("Enter Your Password again: ")
            else:
                ins = Sign_up(first_name, last_name, username, password_1)
                new_reg = {"FirstName": ins.fname, "LastName": ins.lname, "UserName": ins.user_name,
                           "Password": ins.password}
                if choice == "1":
                    logging.info(f'{first_name}{last_name} is Registered as Responsible for Training')
                    print("You Are Registered as Responsible for Training")
                    path = FileHandler("List_of_Staff.csv")
                else:
                    logging.info(f'{first_name}{last_name} is Registered as Professor')
                    print("You Are Registered as Professor")
                    path = FileHandler("List_of_Professor.csv")
                path.add_to_file(new_reg)
                select = False
        elif choice == "2":
            Sign_up.student = True
            first_name = input("Enter Your First Name: ").lower().replace(" ", "")
            last_name = input("Enter Your Last Name: ").lower().replace(" ", "")
            username = input("Enter Your User Name: ").lower().replace(" ", "")
            if os.path.isfile("List_of_Student.csv"):
                reader = FileHandler("List_of_Student.csv")
                result = reader.read_file()
                for i in result:
                    while i["UserName"] == username:
                        logging.info(f'{username} exists')
                        print(''''
                                this username exist,
                                please choose another username''')
                        username = input("Enter Your User Name: ").lower().replace(" ", "")
            else:
                continue
            password_1 = input("Enter Your Password: ")
            password_2 = input("Enter Your Password again: ")
            while password_1 != password_2:
                logging.warning(f'your password is wrong ')
                password_1 = input("Enter Your Password: ")
                password_2 = input("Enter Your Password again: ")
            else:
                ins = Sign_up(first_name, last_name, username, password_1)
                logging.info(f'{first_name}{last_name} is Registered as student')
                print("You Are Registered as Student")
                file_2 = {"FirstName": ins.fname, "LastName": ins.lname, "UserName": ins.user_name,
                          "Password": ins.password, "StudentId": ins.student_code}
                path_2 = FileHandler("List_of_Student.csv")
                path_2.add_to_file(file_2)
                select = False
        else:
            select = False
