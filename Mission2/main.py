# Parent Class

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


# Child Class

class Student(Person):

    def __init__(self, name, age, course, marks):

        # Inheriting from Person class
        super().__init__(name, age)

        self.course = course
        self.marks = marks


    # Method to display student details
    def display(self):

        print("----------------------")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)

        print("Marks :")

        # Dictionary Loop
        for subject, score in self.marks.items():

            print(subject, ":", score)


# Error Handling

try:

    # Creating Student Objects

    student1 = Student(
        "Anushka",
        19,
        "Python",
        {
            "Python": 90,
            "AI": 85
        }
    )

    student2 = Student(
        "Rahul",
        20,
        "Data Science",
        {
            "Python": 78,
            "Maths": 88
        }
    )


    # List of Students

    students = [student1, student2]


    # Loop Through Students

    for student in students:

        student.display()


except Exception as error:

    print("Error:", error)