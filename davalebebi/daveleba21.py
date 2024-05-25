import json


class Student:
    def __init__(self, name, age, grade: []):
        self.name = name
        self.age = age
        self.grade = grade

    def readJson(self):
        with open('students.json', 'r') as students:
            std = json.load(students)
            print(std)

    def average(self):
        with open('students.json', 'r') as students:
            std = json.load(students)
            data={}
            for person in std["students"]:
                data.setdefault(person['name'], sum(person['grades']) / len(person['grades']))
            print(data)

        def writeJson():
            with open('davaleba21.json', 'w') as ans:
                json.dump(data, ans, indent=2)

        return writeJson








student1 = Student('nika', 19, [21, 22, 23, 24, 25, 26])
test=student1.average()
test()
