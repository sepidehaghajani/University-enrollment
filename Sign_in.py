import sys, csv
from hashlib import sha256



def sign_in():
    a = sys.argv[1]
    b= sys.argv[2]
    result = sha256(b.encode())
    hashed = result.hexdigest()
    with open('List_of_Staff', 'r') as f:
        reader = csv.reader(f)
        find = False
        for row in reader:
            if row[0] == a:
                find = True
                if hashed == row[1]:
                    pass
                    # print("Correct")
                else:
                    pass
                    # print("Wrong")
            else:
                with open('List_of_Student', 'r') as f:
                    reader = csv.reader(f)
                    find = False
                    for row in reader:
                        if row[0] == a:
                            if hashed == row[1]:
                                pass
                                # print("Correct")
                            else:
                                pass
                                # print("Wrong")

        if not find:
            print("There is not such a username!")