"""
Program to deserialize an object.
"""
from serialize import Student, Address
import json
import sys

class MyJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            args = dict((key.encode('ascii'), value) for key, value in d.items())
            instance = class_(**args)
        else:
            instance = d
        return instance

def object_hook(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key, value) for key, value in d.items())
        instance = class_(**args)
    else:
        instance = d
    return instance

if __name__ == '__main__':
    f = open('myfile.json', )
    studentDecoded = json.load(f, object_hook=object_hook)
    f.close()

    print("Name:",studentDecoded.name,"\n",
          "Age:",studentDecoded.age,"\n",
          "Marks:",studentDecoded.marks,"\n",
          "City:",studentDecoded.address.city,"\n",
          "Pincode:",studentDecoded.address.pincode)
    """
    Returns :-
    
    Name: Rakesh 
    Age: 18 
    Marks: [33.5, 44, 55, 66, 77] 
    City: Pune 
    Pincode: 55555
    
    """
