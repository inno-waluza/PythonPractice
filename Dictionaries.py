##Dictionaries
from cgi import print_arguments
from unicodedata import name


Student = {"name": "innocet waluza",

 "number": "0994921108"
 ,"age": "20"
 ,"nationality": "malawi"}

for Key, value in Student.items():
    print("Key: " + Key)
    print("Value: " + value)



###print(Student["name"])
##print(Student["number"])
##print(Student)