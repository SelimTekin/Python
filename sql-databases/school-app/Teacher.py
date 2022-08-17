class Teacher:

    def __init__(self, id, studentNumber, name, surname, birthdate, gender, branch):
        if id is None: # id belirtilmediyse
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender