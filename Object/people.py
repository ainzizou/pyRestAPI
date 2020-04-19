import json

class People():

    people = [
        {
            'name':'Achmad Zulkarnain',
            'age': '21',
            'gender': 'male',
         },
        {
            'name': 'Akbar Navis',
            'age': '17',
            'gender': 'male',
        },
        {
            'name': 'Khin Lan San',
            'age': '22',
            'gender': 'female',
        }
    ]

    # def __init__(self, name, age, gender):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender

    def walk(self):
        return "This is from People walk from different object"

    def getAll(self):
        return self.people