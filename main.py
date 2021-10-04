import sign_up
from file_Handler import FileHandler
import Sign_in
import logging

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="a",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


list_of_lessons = [{"Name_Lesson": "Engineering Drawing", "Unit": 2,"Professor's Name":"alikamerei" ,"Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Surveying Theory & Practice I", "Unit": 2, "Professor's Name":"zahraalizadeh","Total_Capacity": 20,
                    "Remain_Capacity": 20, "Number_of_obtained": 0},
                   {"Name_Lesson": "Architecture & Urban Design", "Unit": 2, "Professor's Name":"hosseinanoshe","Total_Capacity": 20,
                    "Remain_Capacity": 20, "Number_of_obtained": 0},
                   {"Name_Lesson": "Statics", "Unit": 3, "Professor's Name":"hassanakbari","Total_Capacity": 27, "Remain_Capacity": 27,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Dynamics", "Unit": 3, "Professor's Name":"hassanakbari","Total_Capacity": 27, "Remain_Capacity": 27,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Mechanics Of Materials I", "Unit": 3,"Professor's Name":"hosseinanoshe", "Total_Capacity": 27, "Remain_Capacity": 27,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Mechanics Of Materials II", "Unit": 2, "Professor's Name":"alikamarei","Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Fluid Mechanics", "Unit": 3, "Professor's Name":"zahraalizadeh","Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Geology Lab", "Unit": 1, "Professor's Name":"zahraalizadeh","Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Construction Materials", "Unit": 2, "Professor's Name":"hassanakbari","Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Construction Materials Lab", "Unit": 1, "Professor's Name":"hosseinanoshe","Total_Capacity": 15,
                    "Remain_Capacity": 15, "Number_of_obtained": 0},
                   {"Name_Lesson": "Concrete Technology", "Unit": 2, "Professor's Name":"hosseinanoshe","Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Soil Mechanics", "Unit": 3, "Professor's Name":"zahraalizadeh","Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Soil Mechanics Lab", "Unit": 1, "Professor's Name":"hassanakbari","Total_Capacity": 15, "Remain_Capacity": 15,
                    "Number_of_obtained": 0},
                   {"Name_Lesson": "Hydraulics", "Unit": 2, "Professor's Name":"hassanakbari","Total_Capacity": 20, "Remain_Capacity": 20,
                    "Number_of_obtained": 0}]

# test = FileHandler("list_of_lessons.csv")
# for item in list_of_lessons:
#     test.add_to_file(item)


select = True
while select:
    print('''
        1-Sign Up
        2-Sign In
        3-Sign Out
        Or Enter any Key For Exit
        ''')
    choice = input('enter your choice: ')
    logging.info("Log in as a User")
    if choice == "1":
        sign_up.registeration()
    elif choice == "2":
        a = input("Enter Your UserName: ").lower().replace(" ","")
        b = input("Enter Your Password: ")
        Sign_in.sign_in(a, b)
    else:
        print("Exit")
        logging.info("User Exit from The Program")
        select = False
