import mysql.connector
from datetime import datetime
from connection import connection

class Student:

    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO student(studentNumber, name, surname, birthdate, gender) VALUES(%s, %s, %s, %s, %s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            Student.connection.close()

    @staticmethod  # aynı amaca ait metodlar için
    def saveStudents(students):
        sql = "INSERT INTO student(studentNumber, name, surname, birthdate, gender) VALUES(%s, %s, %s, %s, %s)"
        values = students
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            Student.connection.close()

# ahmet = Student( ("101","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"))
# ahmet.saveStudent()

ogrenciler = [
    ("101","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("102","Ali","Can",datetime(2005, 6, 17),"E"),
    ("103","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("104","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("105","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("106","Ali","Cenk",datetime(2003, 8, 25),"E")
]

Student.saveStudents(ogrenciler)