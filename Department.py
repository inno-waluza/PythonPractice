from turtle import title


class Department():
    def __init__(self, name, surname):
        self.name = name
        self.surname =  surname

    def printDetails(self):
        fullname = self.name + " " + self.surname
        return fullname

class Innocent(Department):
    def __init__(self, name,  surname):
        super().__init__(name, surname)

        inno = Innocent("innocent ", "waluza")
        print(inno.printDetails())       
