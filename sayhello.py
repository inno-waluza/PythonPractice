def say_hello(names):
    for name in names:
        print("hello " + name)
names = ["innocent", "chipiliro"] 
say_hello(names)   
name_add = input("add a name: ")
names.append(name_add)
say_hello(names)    