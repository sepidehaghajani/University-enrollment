from datetime import datetime
from random import randint
from hashlib import sha256
from file_Handler import FileHandler


class Sign_up:

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = self.hashible(password)
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
        choice = int(input('enter your choice: '))
        if choice == 1:
            username = input("Enter Your User Name: ")
            password_1 = input("Enter Your Password: ")
            password_2 = input("Enter Your Password again: ")
            while password_1 != password_2:
                password_1 = input("Enter Your Password: ")
                password_2 = input("Enter Your Password again: ")
            else:
                ins = Sign_up(username, password_1)
                print("You Are Registered")
                file = [{"UserName": ins.user_name, "Password": ins.password}]
                path = FileHandler("List_of_Staff.csv")
                for item in file:
                    path.add_to_file(item)
                select = False
        elif choice == 2:
            username = input("Enter Your User Name: ")
            password_1 = input("Enter Your Password: ")
            password_2 = input("Enter Your Password again: ")
            while password_1 != password_2:
                password_1 = input("Enter Your Password: ")
                password_2 = input("Enter Your Password again: ")
            else:
                ins = Sign_up(username, password_1)
                print("You Are Registered")
                file = [{"UserName": ins.user_name, "Password": ins.password, "StudentId": ins.student_code}]
                path = FileHandler("List_of_Student.csv")
                for item in file:
                    path.add_to_file(item)
                select = False
        else:
            select = False
