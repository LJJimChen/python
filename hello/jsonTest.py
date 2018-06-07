import json
d = {"name": "1", "age": 11}
print d
# help(json)
print d.popitem()
j = json.dumps(d)
print j


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
studentJson = json.dumps(s, default=lambda obj: obj.__dict__)
print(studentJson)  #序列化类Student


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print json.loads(studentJson, object_hook=dict2student)
