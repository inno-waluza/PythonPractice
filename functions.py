##functions
first_name = input("enter your first name: ")
surname = input("enter your surname: ")
def greetings(first_name, surname):
    print("hello " + first_name.title() + " " + surname.title())
    print("how are you doing " + first_name)
#calling a function    
greetings(first_name, surname)    