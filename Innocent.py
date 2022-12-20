import Department

class Innocent(Department):
    def __init__(self, name,  surname):
        super().__init__(name, surname)

        inno = Innocent("innocent ", "waluza")
        print(inno.printDetails())       
