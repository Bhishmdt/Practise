"""
Serialize using pickle.
"""

import pickle

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

    def print_name(self):
        print(self.name)

if __name__ == '__main__':
    objAdd = Address("Pune", 55555)
    objStudent = Student("Rakesh", 18, [33.5, 44, 55, 66, 77], objAdd)

    P = pickle.dumps(objStudent)
    print(P)
    # Prints b'\x80\x04\x95\x90\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x07Student\x94\x93\x94)\x81\x94}\x94(\x8c\x04name\x94\x8c\x06Rakesh\x94\x8c\x03age\x94K\x12\x8c\x05marks\x94]\x94(G@@\xc0\x00\x00\x00\x00\x00K,K7KBKMe\x8c\x07address\x94h\x00\x8c\x07Address\x94\x93\x94)\x81\x94}\x94(\x8c\x04city\x94\x8c\x04Pune\x94\x8c\x07pincode\x94M\x03\xd9ubub.'
    print(len(P))
    # Prints 155
    # Size of file is 155 bytes

    out_file = open("myfile.pkl", "wb")
    pickle.dump(objStudent, out_file)
    out_file.close()