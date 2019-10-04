import sys
if (sys.version_info.major < 3):
    print("You have to install python 3 version if you want to run this program.")
    quit()
import getpass
import time
from admin import *
from student import *
admin=AdminDatabase()
data=StudentDataBase()
while True:
    print("""WELCOME ! \nPLEASE CHOOSE: \n1 - QUIT \n2 - CREATE ADMIN \n3 - SHOW ADMINS \n4 - LOG IN \n""")
    chose = int(input(":"))
    if chose == 1:
        print("Please wait")
        time.sleep(2)
        break
    elif chose == 2:
        print("Autorization needs to be 'yes' or 'no'")
        admin_id = int(input("Admin id: "))
        admin_namesurname = input("Admin name and surname: ")
        admin_pass = getpass.getpass("Admin Password: ")
        admin_autorization = input("Autorization: ")
        create_admin = Admin(admin_id,admin_namesurname,admin_pass,admin_autorization)
        print("Creating....")
        time.sleep(2)
        admin.create_admin(create_admin)
        print("Created")
    elif chose == 3:
        print("Please wait!")
        time.sleep(2)
        admin.all_admin()
    elif chose == 4:
        while True:
            confirm = input("If you want to return press y/Y or if you don't n/N: ")
            try:
                if confirm.lower() == "y":
                    time.sleep(1)
                    break
                elif confirm.lower() == "n":
                    time.sleep(1)
                    while True:
                        admin_username = input("Name Surname: ")
                        admin_pass = getpass.getpass("Admin Password: ")
                        adminlogusername=admin.admin_nick(admin_username)
                        adminlogpass = admin.admin_pass(admin_pass)
                        time.sleep(2)
                        if adminlogusername == True: 
                            if adminlogpass == True:
                                print("True !")
                                time.sleep(2)
                                if admin.admin_autorization(admin_username):
                                    while True:
                                        print(f"""WELCOME {admin_username} admin! \nPLEASE CHOOSE: \n1 - QUIT \n2 - ADD STUDENT  \n3 - UPDATE STUDENT PROPERTY \n4 - DELETE STUDENT \n5 - SEARCH STUDENT \n6 - SHOW ALL STUDENTS \n""")
                                        try:
                                            make_decision = int(input(": "))
                                            if make_decision == 1:
                                                print("Please wait..")
                                                time.sleep(3)
                                                break
                                            elif make_decision == 2:
                                                search_id = int(input("ID: "))
                                                name = input("Name and Surname: ")
                                                bed = int(input("Please give a bed number: "))
                                                print("Creating student..")
                                                time.sleep(1)
                                                stud = Student(search_id,name,bed)
                                                data.create_student(stud)
                                                print("Created")
                                            elif make_decision == 3:
                                                n_bed = int(input("New Bed Number: "))
                                                bed = int(input("Old Bed Number: "))
                                                time.sleep(1)
                                                data.update_student(n_bed,bed)
                                            elif make_decision == 4:
                                                bed =int(input("Bed Number: "))
                                                time.sleep(1)
                                                data.delete_student(bed)
                                            elif make_decision == 5:
                                                student = int(input("Bed number: "))
                                                print("Wait")
                                                time.sleep(1)
                                                data.search_student(student)
                                            elif make_decision == 6:
                                                print("Wait")
                                                time.sleep(1)
                                                data.all_student()
                                        except:
                                            print("Wrong input!")
                                else:
                                    while True:
                                        print("""WELCOME {}! \nPLEASE CHOOSE: \n1 - QUIT \n2 - ADD STUDENT (needs to be admin)  \n3 - UPDATE STUDENT PROPERTY (needs to be admin) \n4 - DELETE STUDENT (needs to be admin)\n5 - SEARCH STUDENT \n6 - SHOW ALL STUDENTS \n""".format(admin_username))
                                        try:
                                            make_decision = int(input(": "))
                                            if make_decision == 1:
                                                print("Please wait..")
                                                time.sleep(3)
                                                break
                                            elif make_decision == 5:
                                                student = int(input("Bed number: "))
                                                print("Wait")
                                                time.sleep(1)
                                                data.search_student(student)
                                            elif make_decision == 6:
                                                print("Wait")
                                                time.sleep(1)
                                                data.all_student()
                                        except:
                                            print("Wrong input!")
                            else:
                                print("Password is not correct!")
                                time.sleep(2)
                                break
                        else:
                            print("Name and Surname is not correct!")
                            time.sleep(2)
                            break   
            except:
                print("Wrong input bud!")