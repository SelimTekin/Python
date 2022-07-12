# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")

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
    
    @staticmethod
    def saveStudentInfo():
        sql = "select * from student limit 5" # limit 5 -> 5 tane kayıtla sınırlandırılır
        # sql = "select studentNumber, name, surname from student" # Mantıklı olan bu şekilde yani sadece lazım olan alanları almak
        # sql = "select name, surname from student where gender='K'"
        # sql = "select * from student where year(birthdate)=2003"
        # sql = "select * from student where year(birthdate)=2005 and name='Ali'"
        # sql = "select * from student where name like '%an%' or surname like '%an%'"
        # sql = "select count(*) from student where gender='E'"
        # sql = "select name, surname from student where gender='K' order by name,surname"
        Student.mycursor.execute(sql)

        try:
            # results = Student.mycursor.fetchone() # g şıkkı için
            # print(results)

            results = Student.mycursor.fetchall()
            for result in results:
                print(f"{result}") # Artık bir liste değil tuple şeklinde gelir.
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

# Student.saveStudents(ogrenciler)

# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.


Student.saveStudentInfo()