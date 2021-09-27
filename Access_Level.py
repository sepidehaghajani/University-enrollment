import logging
from file_Handler import FileHandler
import csv
from prettytable import PrettyTable
import pandas as pd
import os

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="a",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')


def access_ResponsibleTraining():
    h = True
    while h:
        print('''
        *******************************************
        * You Came in as Responsible for Training *
        *******************************************    
            1-Definition of Lesson
            2-View List of Lessons
            3-View List of Students
            4-Search into List of Lessons
            5-Search into List of Students
            6-View Total Units
            7-View Selected Lessons by Student
            8-View Students Who Have Chosen a Course
            9-Reject or Confirm confirmed lessons
            10-For Exit, Press 10 or any key
            ''')
        # try:
        choice = input("Please Select Your Choice: ")
        if choice == "1":
            y = True
            while y:
                dic = {}
                a = input("Enter Lesson Name: ").capitalize()
                reader = FileHandler("list_of_lessons.csv")
                result = reader.read_file()
                for i in result:
                    while i["Name_Lesson"] == a:
                        logging.info(f'{a} is Repetitive')
                        print(''''
                                this lesson name exist,
                                please enter another lesson''')
                        a = input("Enter Lesson Name: ").capitalize()
                b = int(input("Enter Unit of Lesson: "))
                c = int(input("Enter Total Capacity for This Lesson: "))
                d = input("Enter Professor's Name: ")
                dic["Name_Lesson"] = a
                dic["Unit"] = b
                dic["Professor's Name"] = d
                dic["Total_Capacity"] = c
                dic["Remain_Capacity"] = c
                dic["Number_of_obtained"] = 0
                with open("list_of_lessons.csv", "a") as f:
                    write = csv.DictWriter(f, fieldnames=["Name_Lesson", "Unit", "Professor's Name", "Total_Capacity",
                                                          "Remain_Capacity", "Number_of_obtained"])
                    if f.tell() == 0:
                        write.writeheader()
                    write.writerows([dic])
                    logging.info(f'{a} lesson added to list of lessons ')
                q = input("Do You Want to Register other New Lesson: select(Y/N) ").lower()
                if q == "y":
                    y = True
                else:
                    y = False
        elif choice == "2":

            df = pd.read_csv("list_of_lessons.csv")
            print(df)
            # from prettytable import from_csv
            # with open("list_of_lessons.csv", "r") as fp:
            #     mytable = from_csv(fp)
            #     print(mytable)
        elif choice == "3":

            df = pd.read_csv("List_of_Student.csv")
            print(df)
            # from prettytable import from_csv
            # with open("List_of_Student.csv", "r") as fp:
            #     mytable = from_csv(fp)
            #     print(mytable)
        elif choice == "4":
            lesson_name = input("Enter your desired lesson: ").capitalize()
            read_lessons = pd.read_csv("list_of_lessons.csv")
            for ind, item in read_lessons.iterrows():
                if item["Name_Lesson"] == lesson_name:
                    mytable = PrettyTable(
                        ['Name_Lesson', 'Unit', "Professor's Name", "Total_Capacity", "Remain_Capacity",
                         "Number_of_obtained"])
                    lis = [item['Name_Lesson'], item["Unit"], item["Professor's Name"], item["Total_Capacity"],
                           item["Remain_Capacity"], item["Number_of_obtained"]]
                    mytable.add_row(lis)
                    print(mytable)
                    logging.info(f"search based on {lesson_name} done successfully")
                else:
                    print("This Lesson don't Exist")
                    logging.info(f"search based on {lesson_name} done Unsuccessfully")

        elif choice == "5":
            print('''
                    1-Student Name
                    2-Student Code
                    ''')
            search = input("Your Search Based on: ")
            if search == "1":
                search_name = input("Enter Your The Desired Name: ").lower().replace(" ", "")
                reader = FileHandler("List_of_Student.csv")
                result = reader.read_file()
                for i in result:
                    find = False
                    if i["UserName"] == search_name:
                        logging.info(f'the student with username {search_name}is found')
                        find = True
                        mytable = PrettyTable(['UserName', 'StudentId'])
                        lis = [i['UserName'], i["StudentId"]]
                        mytable.add_row(lis)
                        print(mytable)

                if not find:
                    print("There is not such a username!")
            else:
                search_student_code = input("Enter Your The Desired Student Code: ").lower().replace(" ", "")
                reader = FileHandler("List_of_Student.csv")
                result = reader.read_file()
                for i in result:
                    find = False
                    if i["StudentId"] == search_student_code:
                        logging.info(f'the student with this code {search_student_code} is found')
                        find = True
                        mytable = PrettyTable(['UserName', 'StudentId'])
                        lis = [i['UserName'], i["StudentId"]]
                        mytable.add_row(lis)
                        print(mytable)

                if not find:
                    print("There is not such a student!")
        elif choice == "6":
            df2 = pd.read_csv('list_of_lessons.csv')
            summ=df2['Unit'].sum()
            print(f'Sum Total Units is : {summ} ')


        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        else:
            print("Exit")
            logging.info("User Exit from The Program")
            h = False
    # except Exception as e:
    #     print(e)


def access_Student(a):
    storage_path = 'Students_files'
    if os.path.exists(storage_path):
        print('Directory exist')

    else:
        os.mkdir(storage_path)
        print('Directory Created')

    h = True

    while h:
        print('''
        **************************
        * You Came in as Student *
        **************************   
                1-View List of Lessons
                2-Select Lesson
                3-Search into List of Lessons
                4-View Selected Lessons and Summation of Units
                5-View Reject or Confirm of Selected lessons
                ''')

        choice = input("Please Select Your Choice: ")
        if choice == "1":
            df = pd.read_csv("list_of_lessons.csv")
            print(df)
            # from prettytable import from_csv
            # with open("list_of_lessons.csv", "r") as fp:
            #     mytable = from_csv(fp)
            #     print(mytable)
        elif choice == "2":
            df = pd.read_csv("list_of_lessons.csv")
            print(df)

            user_input = input("Enter Your Desirable Lesson: ")
            if os._exists(f'cartabl{a}.csv'):
                check = pd.read_csv(f'cartabl{a}.csv')
                for Index, Row in check.iterrows():
                    if Row["Name_Lesson"] != user_input:
                        continue
                    else:
                        raise (f'You Selected This Lesson Before ')
            for index, row in df.iterrows():
                if row["Name_Lesson"] == user_input and row["Remain_Capacity"] > 0:
                    dic = {}
                    select_lesson = {}
                    select_lesson["Name_Lesson"] = user_input
                    select_lesson["Unit"] = row["Unit"]
                    select_lesson["Total_Capacity"] = row["Total_Capacity"]
                    select_lesson["Number_of_obtained"] = row["Number_of_obtained"] + 1
                    select_lesson["Remain_Capacity"] = row["Total_Capacity"] - select_lesson["Number_of_obtained"]
                    # select_lesson["limitation_of_select"]=row["Unit"]
                    # print(select_lesson)
                    df.loc[index, "Remain_Capacity"] = select_lesson["Remain_Capacity"]
                    df.loc[index, "Number_of_obtained"] = select_lesson["Number_of_obtained"]
                    df.to_csv("list_of_lessons.csv", index=False)
                    dic["Name_Lesson"] = select_lesson["Name_Lesson"]
                    dic["Unit"] = select_lesson["Unit"]
                    dic["Confirmed"] = False
                    dic["Rejected"] = False

                    s = os.path.join(storage_path, f'cartabl{a}.csv')
                    with open(s, "a", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=["Name_Lesson", "Unit", "Confirmed", "Rejected"])
                        if f.tell() == 0:
                            writer.writeheader()
                        writer.writerow(dic)
        elif choice == "3":
            lesson_name = input("Enter your desired lesson: ").capitalize()
            read_lessons = pd.read_csv("list_of_lessons.csv")
            for ind, item in read_lessons.iterrows():
                if item["Name_Lesson"] == lesson_name:
                    mytable = PrettyTable(
                        ['Name_Lesson', 'Unit', "Professor's Name", "Total_Capacity", "Remain_Capacity",
                         "Number_of_obtained"])
                    lis = [item['Name_Lesson'], item["Unit"], item["Professor's Name"], item["Total_Capacity"],
                           item["Remain_Capacity"], item["Number_of_obtained"]]
                    mytable.add_row(lis)
                    print(mytable)
                    logging.info(f"search based on {lesson_name} done successfully")
                else:
                    print("This Lesson don't Exist")
                    logging.info(f"search based on {lesson_name} done Unsuccessfully")



        elif choice == "4":
            jj=pd.read_csv(f'Students_files/cartabl{a}.csv')
            print(jj)
            df2 = pd.read_csv(f'Students_files/cartabl{a}.csv')
            summ = df2['Unit'].sum()
            print(f'Sum Total Units is : {summ} ')

        elif choice == "5":
            pass

        else:
            print("Exit")
            logging.info("User Exit from The Program")
            h = False


#
# access_ResponsibleTraining()
access_Student("mr.rahmani")
