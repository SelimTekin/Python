class Student:

    def __init__(self, id, studentNumber, name, surname, birthdate, gender, classid):
        if id is None: # id belirtilmediyse
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        if len(name) > 45:
            raise Exception("name için maksimumu 45 karakter girmelisiniz.")
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid

    def createStudent(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return list