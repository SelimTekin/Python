import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "select * from student where id=%s"
        value = (id,)
        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchone()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def getStudentByClassId(self, classid):
        sql = "select * from student where classid=%s"
        value = (classid,)
        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO student(studentNumber, name, surname, birthdate, gender, classid) VALUES(%s, %s, %s, %s, %s, %s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            self.connection.close()

    def editStudent(self, student: Student):
        sql = "update student set studentNumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid=%s where id=%s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            self.connection.close()

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
         

db = DbManager()

student = db.getStudentById(2)

student[0].name = "Mehmet"
# student[0].surname = "Turan"
# student[0].studentNumber = "501"

# db.addStudent(student[0])
db.editStudent(student[0])

# print(student[0].name)
# print(student[0].surname)

# students = db.getStudentByClassId(1)
# print(students[0].name)
# print(students[4].name)