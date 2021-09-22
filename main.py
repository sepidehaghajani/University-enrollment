import sign_up
from file_Handler import FileHandler
import Sign_in

list_of_lessons = [{"Name_Lesson": "Engineering Drawing", "Unit": 2, "Total_Capacity": 20},
                   {"Name_Lesson": "Surveying Theory & Practice I", "Unit": 2, "Total_Capacity": 20},
                   {"Name_Lesson": "Architecture & Urban Design", "Unit": 2, "Total_Capacity": 20},
                   {"Name_Lesson": "Statics", "Unit": 3, "Total_Capacity": 27},
                   {"Name_Lesson": "Dynamics", "Unit": 3, "Total_Capacity": 27},
                   {"Name_Lesson": "Mechanics Of Materials I", "Unit": 3, "Total_Capacity": 27},
                   {"Name_Lesson": "Mechanics Of Materials II", "Unit": 2, "Total_Capacity": 20},
                   {"Name_Lesson": "Fluid Mechanics", "Unit": 3, "Total_Capacity": 20},
                   {"Name_Lesson": "Geology Lab", "Unit": 1, "Total_Capacity": 20},
                   {"Name_Lesson": "Construction Materials", "Unit": 2, "Total_Capacity": 20},
                   {"Name_Lesson": "Construction Materials Lab", "Unit": 1, "Total_Capacity": 15},
                   {"Name_Lesson": "Concrete Technology", "Unit": 2, "Total_Capacity": 20},
                   {"Name_Lesson": "Soil Mechanics", "Unit": 3, "Total_Capacity": 20},
                   {"Name_Lesson": "Soil Mechanics Lab", "Unit": 1, "Total_Capacity": 15},
                   {"Name_Lesson": "Hydraulics", "Unit": 2, "Total_Capacity": 20}]

test = FileHandler("list_of_lessons.csv")
for item in list_of_lessons:
    test.add_to_file(item)


select = True
while select:
    print('''
        1-Sign Up
        2-Sign In
        3-Sign Out
        Or Enter Every Key For Exit
        ''')
    choice = int(input('enter your choice: '))

    if choice == 1:
        sign_up.registeration()
    elif choice == 2:
        # a = input("Enter Your UserName: ")
        # b = input("Enter Your Password: ")
        Sign_in.sign_in()
    else:
        print("Exit")
        select = False
