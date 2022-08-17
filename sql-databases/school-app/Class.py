class Class:

    def __init__(self, id, name, teacherid):
        if id is None: # id belirtilmediyse
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid