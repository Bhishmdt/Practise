"""
Program to serialize an object.
"""
import json

class Address(object):
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

class Student(object):
    def __init__(self, name, age, marks, address):
        self.name = name
        self.age = age
        self.marks = marks
        self.address = address

class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        d = {}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d

if __name__ == '__main__':
    objAdd = Address("Pune", 55555)
    objStudent = Student("Rakesh", 18, [33.5, 44, 55, 66, 77], objAdd)

    print(json.dumps(objStudent, cls=MyJSONEncoder))
    # Prints {"__class__": "Student", "__module__": "__main__", "name": "Rakesh", "age": 18, "marks": [33.5, 44, 55, 66, 77], "address": {"__class__": "Address", "__module__": "__main__", "city": "Pune", "pincode": 55555}}

    out_file = open("myfile.json", "w")
    json.dump(objStudent, out_file, cls=MyJSONEncoder)
    out_file.close()