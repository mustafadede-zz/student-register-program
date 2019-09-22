import sys
if (sys.version_info.major < 3):
    print("You have to install python 3 version if you want to run this program.")
    quit()
import time
from student import *
print("""
WELCOME !
PLEASE CHOOSE:
1 - QUIT
2 - ADD STUDENT
3 - UPDATE STUDENT PROPERTY
4 - DELETE STUDENT
5 - SHOW ALL STUDENTS
""")
data=DataBase()
while True:
    try:
        make_decision = int(input(": "))
        if make_decision == 1:
            print("Please wait..")
            time.sleep(3)
            break
        if make_decision == 2:
            search_id = int(input("ID: "))
            name = input("Name and Surname: ")
            bed = int(input("Please give a bed number: "))
            stud = Student(search_id,name,bed)
            data.create_student(stud)
        if make_decision == 3:
            n_bed = int(input("New Bed Number: "))
            bed = int(input("Old Bed Number: "))
            data.update_student(n_bed,bed)
        if make_decision == 4:
            bed =int(input("Bed Number: "))
            data.delete_student(bed)
        if make_decision == 5:
            data.all_student()
    except:
        print("Wrong!")