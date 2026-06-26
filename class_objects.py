class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Mark :", self.mark)

    def result(self):
        if self.mark >= 50:
            print("Result : Pass")
        else:
            print("Result : Fail")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
mark = int(input("Enter Mark: "))
student1 = Student(name, age, mark)
student1.display()
student1.result()