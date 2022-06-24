# Inheritance (Kalıtım)

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname  # self.firstname: dışarıdan gelen name bilgisi
        self.lastname = lname
        print('Person created')
    
    def who_am_i(self):
        print('I am person')

    def eat(self):
        print('I am eating')

class Student(Person):
    # def __init__(self, fname, lname):
    #     super().__init__(fname, lname)

    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student created')

    def sayHello(self):
        print('Hello i am a student')

    # override
    def who_am_i(self):
        print('I am student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) #super ile çağırdığımız zaman self yazmaya gerek yok
        self.branch = branch

    def who_am_i(self):
        print(f'I am {self.branch} teacher')


p1 = Person('Selim', 'Tekin')
s1 = Student('Enes', 'Dönmez', 1256)
t1 = Teacher('Selim', 'Tekin', 'Math')

t1.who_am_i()
print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNumber))


p1.who_am_i()
s1.who_am_i()
s1.sayHello() #Student class'ına ait Person'a özgü metot değil
p1.eat()
s1.eat()