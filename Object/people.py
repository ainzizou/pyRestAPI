class People(object):

    peopleList = []

    # Put name = None to define if the arguments not passed in the constructor
    def __init__(self, name=None, age=None, gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    # def serialize(self):
    #     return {
    #         'name': self.name,
    #         'age': self.age,
    #         'gender': self.gender,
    #     }

    def walk(self):
        return "This is from People walk from different object"

    def getAll(self):
        return self.peopleList

    def addPeople(obj):
        People.peopleList.append(obj)
        return obj.getAll()