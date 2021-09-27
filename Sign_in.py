import logging
import sys, csv
from hashlib import sha256
import Access_Level

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="a",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def sign_in(a, b):
    result = sha256(b.encode())
    hashed = result.hexdigest()
    with open('List_of_Staff.csv', 'r') as f:
        reader = csv.DictReader(f)
        find = False
        for row in reader:
            if row["UserName"] == a:
                find = True
                if hashed != row["Password"]:
                    i = 1
                    while hashed != row["Password"] and i <= 3:
                        logging.warning(f'{a}, your password is wrong')
                        b = input('''
                                    your password is wrong 
                                    Please Try Again:
                                     ''')
                        result = sha256(b.encode())
                        hashed = result.hexdigest()
                        i+=1
                    if hashed != row["Password"]:
                        logging.info(f'Your Account is not Accessible. Please Try 5 min Later')
                    else:
                        Access_Level.access_ResponsibleTraining()
                else:
                    Access_Level.access_ResponsibleTraining()

            else:
                continue
    with open('List_of_Student.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["UserName"] == a:
                find = True
                if hashed != row["Password"]:
                    i = 1
                    while hashed != row["Password"] and i <= 3:
                        logging.warning(f'{a}, your password is wrong')
                        b = input('''
                                    your password is wrong 
                                    Please Try Again:
                                     ''')
                        result = sha256(b.encode())
                        hashed = result.hexdigest()
                        i += 1
                    if hashed != row["Password"]:
                        logging.info(f'Your Account is not Accessible. Please Try 5 min Later')
                    else:
                        Access_Level.access_Student(a)
                else:
                    Access_Level.access_Student(a)

        if not find:
            print("There is not such a username!")
