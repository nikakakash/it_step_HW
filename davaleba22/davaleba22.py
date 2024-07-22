from faker  import Faker
import json




class fakess():
    def __init__(self):
        self.fake = Faker()
        self.data_list = []
    def fakeNum(self,num):
        for person in range(0, num + 1):
            name = self.fake.name()
            email = self.fake.email()
            grade = self.fake.random_int(0, 10)
            self.data_list.append({'name': name, 'email': email, 'grade': grade})
        return self.data_list

    def addToJson(self,json_data, file_name):
        with open(file_name, 'w') as file:
            json.dump(json_data, file, indent=2)



    def readJson(self,file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            data.sort(key=lambda x: x['grade'], reverse=True)
            print(data)


fakee = fakess()
fakee.addToJson(fakee.fakeNum(num=100),'data.jsno')
fakee.readJson('data.json')



