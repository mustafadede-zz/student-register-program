import sqlite3
#STUDENT STUFF
class Student():
    def __init__(self,search_id=None,namesurname=None,bed_number=None):
        self.namesurname=namesurname
        self.bed_number=bed_number
        self.search_id=search_id
    def __str__(self):
        return f"Name: {self.namesurname} \nSearch Id: {self.search_id} \nBed number: {self.bed_number}"
#STUDENT DATABASE STUFF
class StudentDataBase():
    def __init__(self):
        self.connection()
    def connection(self):
        self.link = sqlite3.connect("student_database.db")
        self.cursor = self.link.cursor()
        self.cursor.execute("Create table If not exists STUDENT (search_id integer,name_surname text,bed_number integer PRIMARY_KEY)")
        self.link.commit()
    def disconnection(self):
        self.link.close()
    #CREATE A STUDENT
    def create_student(self,Student):
        self.cursor.execute("Insert into STUDENT Values(?,?,?)",(Student.search_id,Student.namesurname,Student.bed_number))
        self.link.commit()
    #USING BED NUMBER FOR DELETE STUDENT
    def delete_student(self,bed_number):
        self.cursor.execute("Delete from STUDENT where bed_number= ?",(bed_number,))
        self.link.commit()
    #UPDATE STUDENT BED NUMBER
    def update_student(self,new_bed,bed_number):
        self.cursor.execute("Update STUDENT set bed_number= ? where bed_number = ?",(new_bed,bed_number,))
        self.link.commit()
    #SHOW ALL STUDENT
    def all_student(self):
        self.cursor.execute("Select * from STUDENT")
        all_student = self.cursor.fetchall()
        if len(all_student) == 0:
            print("There is no record") 
        else:
            total_student=0
            for i in all_student:
                students = Student(i[0],i[1],i[2])
                total_student+=1
                print(students)
                print("  --  ")
            print("Total Student = "+str(total_student))
    # SPECIFIC SEARCH
    def search_student(self,bed_number):
        self.cursor.execute("Select name_surname,search_id from STUDENT where bed_number=?",(bed_number,)) 
        student = self.cursor.fetchall()
        for i in student:
            print("Name and Surname: " + str(i[0])+"\n"+"Search id: " + str(i[1]))
        self.link.commit()