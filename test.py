class Person():

    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print("test: ",self.name)
        print("test: ",self.id_number)

class Employee(Person):
    def __init__(self,name, id_number,salary, post):

        super().__init__(name, id_number)
        self.salary = salary
        self.post = post

    def display(self):
        super().display()
        print("test: ",self.salary)
        print("test: ",self.post)
        
test = Employee("stuff","test","idk","uuhh")

test.display()