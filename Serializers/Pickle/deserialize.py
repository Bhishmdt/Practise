"""
Deserialize using pickle.
"""
import pickle
from serialize import Student, Address

if __name__ == '__main__':
    f = open('myfile.pkl', 'rb')
    studentDecoded = pickle.load(f)
    f.close()
    print("Name:", studentDecoded.name, "\n",
          "Age:", studentDecoded.age, "\n",
          "Marks:", studentDecoded.marks, "\n",
          "City:", studentDecoded.address.city, "\n",
          "Pincode:", studentDecoded.address.pincode)
    print("Print using function:", end=" ")
    studentDecoded.print_name()
    """
    
    Returns :-
    
    Name: Rakesh 
    Age: 18 
    Marks: [33.5, 44, 55, 66, 77] 
    City: Pune 
    Pincode: 55555
    Print using function:: Rakesh
    
    """
