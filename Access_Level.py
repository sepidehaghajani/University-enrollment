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
            6-View Total Presented Units
            7-View Selected Lessons by Students
            8-View Students Who Have Chosen a Specified Lesson
            9-View Specified Student Caretable
            10-Reject or Confirm confirmed lessons
            11-For Exit, Press 11 or any key
            ''')
        # try:
        choice = input("Please Select Your Choice: ")
        if choice == "1":  # Definition of Lesson
            y = True
            while y:
                dic = {}
                a = input("Enter Lesson Name: ").capitalize()
                reader = FileHandler("list_of_lessons.csv")
                result = reader.read_file()
                for i in result:
                    while i["Name_Lesson"] == a:
                        logging.info(f'{a} is Repetitive')
                        print('''
                                this lesson name exist,
                                please enter another lesson
                                ''')
                        a = input("Enter Lesson Name: ").capitalize()
                b = int(input("Enter Unit of Lesson: "))
                c = int(input("Enter Total Capacity for This Lesson: "))
                d = input("Enter Professor's Name: ").lower().replace(" ", "")
                dic["Name_Lesson"] = a
                dic["Unit"] = b
                if d == "":
                    dic["Professor's Name"] = "None"
                else:
                    dic["Professor's Name"] = d
                dic["Total_Capacity"] = c
                dic["Remain_Capacity"] = c
                dic["Number_of_obtained"] = 0
                with open("list_of_lessons.csv", "a") as f:
                    write = csv.DictWriter(f, fieldnames=["Name_Lesson", "Unit", "Professor's Name", "Total_Capacity",
                                                          "Remain_Capacity", "Number_of_obtained"])
                    if f.tell() == 0:
                        write.writeheader()
                    write.writerow(dic)
                    logging.info(f'{a} lesson added to list of lessons ')
                q = input("Do You Want to Register other New Lesson: select(Y/N) ").lower()
                if q == "y":
                    y = True
                else:
                    y = False

        elif choice == "2":  # View List of Lessons
            df = pd.read_csv("list_of_lessons.csv")
            print(df)
            # from prettytable import from_csv
            # with open("list_of_lessons.csv", "r") as fp:
            #     mytable = from_csv(fp)
            #     print(mytable)



        elif choice == "3":  # View List of Students

            df = pd.read_csv("List_of_Student.csv")
            print(df)
            # from prettytable import from_csv
            # with open("List_of_Student.csv", "r") as fp:
            #     mytable = from_csv(fp)
            #     print(mytable)
        elif choice == "4":  # Search into List of Lessons
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

        elif choice == "5":  # Search into List of Students
            print('''
                    1-Student Name
                    2-Student Code
                    ''')
            search = input("Your Search Based on: ")
            find = False
            if search == "1":
                search_name = input("Enter Your The Desired Name: ").lower().replace(" ", "")
                reader = FileHandler("List_of_Student.csv")
                result = reader.read_file()
                for i in result:
                    if i["FirstName"] + i["LastName"] == search_name:
                        logging.info(f'the student with username {search_name}is found')
                        find = True
                        mytable = PrettyTable(['FirstName', 'LastName', 'UserName', 'StudentId'])
                        lis = [i['FirstName'], i['LastName'], i['UserName'], i["StudentId"]]
                        mytable.add_row(lis)
                        print(mytable)

                if find:
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
                        mytable = PrettyTable(['FirstName', 'LastName', 'UserName', 'StudentId'])
                        lis = [i['FirstName'], i['LastName'], i['UserName'], i["StudentId"]]
                        mytable.add_row(lis)
                        print(mytable)

                if find:
                    print("There is not such a student!")
        elif choice == "6":  # View Total Presented Units
            df2 = pd.read_csv('list_of_lessons.csv')
            summ = df2['Unit'].sum()
            print(f'Sum Total Presented Units is : {summ} ')


        elif choice == "7":  # View Selected Lessons by Students
            data = pd.read_csv("list_of_lessons.csv")
            data = data[data["Number_of_obtained"] > 0]
            print(data)

        elif choice == "8":  # View Students Who Have Chosen a Specified Lesson
            name_lesson = input("Enter Your The Desired Lesson ")
            data = pd.read_csv("list_student_lesson.csv")
            data = data[data["Name_Lesson"] == name_lesson]
            print(data)
            if not data.empty:
                print(f'''Students Who Have Chosen {name_lesson}:
            {data["First and Last Name"]}
                ''')

            else:
                print("No One!!..")

        elif choice == "9":  # View Specified Student Caretable
            name_student = input("Enter Name of Your The Desired Student").lower().replace(" ", "")
            data = pd.read_csv("list_student_lesson.csv")
            data = data[data["First and Last Name"] == name_student]
            if not data.empty:
                print(data)
            else:
                print("this student don't select lesson yet ")

        elif choice == "10":  # Reject or Confirm confirmed lessons
            df = pd.read_csv("list_student_lesson.csv")
            df = df[df["Lesson_Status"] == "Unknown"]
            print(df)
            if not df.empty:
                q = input("Are You Want To Change Status: (Y/N) ").lower()
                if q == "y":
                    q2 = input("Select Student Name: ").lower().replace(" ", "")
                    df = df[(df["First and Last Name"] == q2) & (df["Lesson_Status"] == "Unknown")]
                    print(df)
                    pl=pd.read_csv("list_student_lesson.csv")
                    for index, row in df.iterrows():
                        dd=input("Enter '1-Confirm' or '2-Reject'")
                        if dd=="1":
                            pl.loc[index, "Lesson_Status"] = "Confirm"
                        else:
                            pl.loc[index, "Lesson_Status"] = "Reject"
                        pl.to_csv("list_student_lesson.csv", index=False)
                        gh = pd.read_csv(f'Students_files/cartabl{row["UserName"]}.csv')
                        for ind,ro in gh.iterrows():
                            if ro["Name_Lesson"]==row["Name_Lesson"]:
                                if dd == "1":
                                    gh.loc[ind,"Lesson_Status"]="Confirm"
                                else:
                                    gh.loc[ind, "Lesson_Status"] ="Reject"
                                gh.to_csv(f'Students_files/cartabl{row["UserName"]}.csv',index=False)
            else:
                print("Nothing Exist")

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

    def ret_user(a):
        with open("List_of_Student.csv", "r") as f:
            read = csv.DictReader(f)
            for item in read:
                if item["UserName"] == a:
                    return item["FirstName"] + item["LastName"]

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
                6-Press any Key for Exit
                ''')

        choice = input("Please Select Your Choice: ")
        if choice == "1":  # View List of Lessons
            df = pd.read_csv("list_of_lessons.csv")
            print(df)
            # from prettytable import from_csv
            # with open("list_of_lessons.csv", "r") as fp:
            #     mytable = from_csv(fp)
            #     print(mytable)
        elif choice == "2":  # Select Lesson
            df = pd.read_csv("list_of_lessons.csv")
            print(df)
            user_input = input("Enter Your Desirable Lesson: ")
            for index, row in df.iterrows():
                if row["Name_Lesson"] == user_input and row["Remain_Capacity"] > 0:
                    if os.path.exists(f'Students_files/cartabl{a}.csv'):
                        check = pd.read_csv(f'Students_files/cartabl{a}.csv')
                        for Index, Row in check.iterrows():
                            if Row["Name_Lesson"] == user_input or (check['Unit'].sum() + row["Unit"]) > 20:
                                raise Exception(
                                    f"You aren't Allowed to Select more than 20 Unit or a Duplicate lesson ")

                        dic = {}
                        dic2 = {}
                        select_lesson = {}
                        select_lesson["Name_Lesson"] = user_input
                        select_lesson["Unit"] = row["Unit"]
                        select_lesson["Total_Capacity"] = row["Total_Capacity"]
                        select_lesson["Number_of_obtained"] = row["Number_of_obtained"] + 1
                        select_lesson["Remain_Capacity"] = row["Total_Capacity"] - select_lesson[
                            "Number_of_obtained"]
                        df.loc[index, "Remain_Capacity"] = select_lesson["Remain_Capacity"]
                        df.loc[index, "Number_of_obtained"] = select_lesson["Number_of_obtained"]
                        df.to_csv("list_of_lessons.csv", index=False)
                        dic["Name_Lesson"] = select_lesson["Name_Lesson"]
                        dic["Unit"] = select_lesson["Unit"]
                        dic2["Name_Lesson"] = select_lesson["Name_Lesson"]
                        dic2["Unit"] = select_lesson["Unit"]
                        dic2["UserName"] = a
                        dic2["First and Last Name"] = ret_user(a)
                        dic2["Lesson_Status"] = "Unknown"  # "Unknown","Confirmed","Rejected"
                        dic["Lesson_Status"] = dic2["Lesson_Status"]  # "Unknown","Confirmed","Rejected"
                        s = os.path.join(storage_path, f'cartabl{a}.csv')
                        with open(s, "a", newline="") as f:
                            writer = csv.DictWriter(f, fieldnames=["Name_Lesson", "Unit", "Lesson_Status"])
                            if f.tell() == 0:
                                writer.writeheader()
                            writer.writerow(dic)
                        with  open("list_student_lesson.csv", "a", newline="") as k:
                            writ = csv.DictWriter(k, fieldnames=["Name_Lesson", "Unit", "UserName",
                                                                 "First and Last Name", "Lesson_Status"])
                            if k.tell() == 0:
                                writ.writeheader()
                            writ.writerow(dic2)

                    else:
                        dic = {}
                        dic2 = {}
                        select_lesson = {}
                        select_lesson["Name_Lesson"] = user_input
                        select_lesson["Unit"] = row["Unit"]
                        select_lesson["Total_Capacity"] = row["Total_Capacity"]
                        select_lesson["Number_of_obtained"] = row["Number_of_obtained"] + 1
                        select_lesson["Remain_Capacity"] = row["Total_Capacity"] - select_lesson["Number_of_obtained"]
                        df.loc[index, "Remain_Capacity"] = select_lesson["Remain_Capacity"]
                        df.loc[index, "Number_of_obtained"] = select_lesson["Number_of_obtained"]
                        df.to_csv("list_of_lessons.csv", index=False)
                        dic["Name_Lesson"] = select_lesson["Name_Lesson"]
                        dic["Unit"] = select_lesson["Unit"]
                        dic2["Name_Lesson"] = select_lesson["Name_Lesson"]
                        dic2["Unit"] = select_lesson["Unit"]
                        dic2["UserName"] = a
                        dic2["First and Last Name"] = ret_user(a)
                        dic2["Lesson_Status"] = "Unknown"  # "Unknown","Confirmed","Rejected"
                        dic["Lesson_Status"] = dic2["Lesson_Status"]  # "Unknown","Confirmed","Rejected"
                        s = os.path.join(storage_path, f'cartabl{a}.csv')
                        with open(s, "a", newline="") as f:
                            writer = csv.DictWriter(f, fieldnames=["Name_Lesson", "Unit", "Lesson_Status"])
                            if f.tell() == 0:
                                writer.writeheader()
                            writer.writerow(dic)
                        with  open("list_student_lesson.csv", "a", newline="") as k:
                            writ = csv.DictWriter(k,
                                                  fieldnames=["Name_Lesson", "Unit", "UserName", "First and Last Name",
                                                              "Lesson_Status"])
                            if k.tell() == 0:
                                writ.writeheader()
                            writ.writerow(dic2)
        elif choice == "3":
            lesson_name = input("Enter your desired lesson: ")
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
            jj = pd.read_csv(f'Students_files/cartabl{a}.csv')
            print(jj)
            summ = jj['Unit'].sum()
            print(f'Sum Total Units is : {summ} ')

        elif choice == "5":
            gh=pd.read_csv(f'Students_files/cartabl{a}.csv')
            print(gh)

        else:
            print("Exit")
            logging.info("User Exit from The Program")
            h = False


def access_Professor(a):
    def ret_user(a):
        with open("List_of_Professor.csv", "r") as f:
            read = csv.DictReader(f)
            for item in read:
                if item["UserName"] == a:
                    return item["FirstName"] + item["LastName"]

    h = True
    while h:
        print('''
        **************************
        * You Came in as Professor *
        **************************   
                1-View List of Lessons   
                2-Search into List of Lessons
                3-View Selected Lessons
                4-Select Lesson
                5-View List of Students Based on Selected Lesson
                6-For Exit, Press 6 or any key
                ''')
        choice = input("Please Select Your Choice: ")
        if choice == "1":  # View List of Lessons

            df = pd.read_csv("list_of_lessons.csv")
            print(df)

        elif choice == "2":  # Search into List of Lessons
            lesson_name = input("Enter your desired lesson: ").capitalize()
            data = pd.read_csv("list_of_lessons.csv")
            data = data[data["Name_Lesson"] == lesson_name]
            print(data)

        elif choice == "3":  # View Selected Lessons
            d = ret_user(a)
            data = pd.read_csv("list_of_lessons.csv")
            data = data[data["Professor's Name"] == d]
            print(data)
        elif choice == "4":  # Select Lesson
            data = pd.read_csv("list_of_lessons.csv")
            data = data[data["Professor's Name"] == "None"]
            print(data)
            summ = data['Unit'].sum()
            count = 0
            df = pd.read_csv("list_of_lessons.csv")

            if summ >= 10:
                c = True
            else:
                c = False
            while c:
                sel = input("Select Name of Your The Desired Lesson From Above List: ")
                for index, row in df.iterrows():
                    if row["Name_Lesson"] == sel:
                        count += row["Unit"]
                        if count <= 15:
                            df.loc[index, "Professor's Name"] = ret_user(a)
                            df.to_csv("list_of_lessons.csv", index=False)
                            data = pd.read_csv("list_of_lessons.csv")
                            data = data[data["Professor's Name"] == "None"]
                            print(data)
                            Que = input("Do You Want to Continue? (Y/N) ").lower()
                            if Que == "y":
                                continue
                            else:
                                c = False
                        else:
                            print("you aren't allowed to select more 15 units ")
                            c = False

        elif choice == "5":  # View List of Students Based on Selected Lesson
            select_name = input("Enter Your Desired Lesson Name: ")
            data = pd.read_csv("list_student_lesson.csv")
            data = data[data["Name_Lesson"] == select_name]
            if not data.empty:
                print(data)
            else:
                print("No one chose this lesson")
        else:
            print("Exit")
            logging.info("User Exit from The Program")
            h = False





# access_ResponsibleTraining()
# access_Student("jahani")

# access_Professor("anoshe")
