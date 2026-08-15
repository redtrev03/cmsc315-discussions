"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.

class ParentClass:
    # Class variable
    category = "Parent"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Category: {self.category}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.

class ChildClass(ParentClass):
    # New class variable
    school = "Generic University"

    def __init__(self, name, age, student_id, major):
        # Initialize the inherited instance variables
        super().__init__(name, age)

        # New instance variables
        self.student_id = student_id
        self.major = major
        self.courses = []

    # New method
    def enroll_course(self, course):
        self.courses.append(course)

    # Override the parent method
    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"ID: {self.student_id}, Major: {self.major}, "
            f"School: {self.school}, Courses: {self.courses}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two objects of the child class
    student1 = ChildClass("Alice", 20, "S100", "Computer Science")
    student2 = ChildClass("Bob", 22, "S101", "Cybersecurity")

    # Access the class variable through the class
    print("Class variable through class:", ChildClass.school)

    # Access the same class variable through an object
    print("Class variable through student1:", student1.school)
    print("Class variable through student2:", student2.school)

    # Add an attribute to only student1
    student1.favorite_color = "Blue"

    # Display each object's namespace
    print("\nstudent1 namespace:")
    print(student1.__dict__)

    print("\nstudent2 namespace:")
    print(student2.__dict__)

    # Display information about the class namespace
    print("\nChildClass namespace:")
    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object
    original = ChildClass(
        "Charlie",
        21,
        "S200",
        "Computer Science"
    )

    # Add nested mutable data
    original.courses = [
        {
            "name": "Python",
            "assignments": [
                "Assignment 1",
                "Assignment 2"
            ]
        }
    ]

    # A shallow copy creates a new outer object,
    # but nested objects are still shared.
    shallow_copy = copy(original)

    # A deep copy creates a new outer object and
    # independently copies all nested objects.
    deep_copy = deepcopy(original)

    # Modify the original object's nested data
    original.courses[0]["assignments"].append("Assignment 3")

    # Display the original object
    print("Original object:")
    print(original.__dict__)

    # Display the shallow copy
    print("\nShallow copy:")
    print(shallow_copy.__dict__)

    # Display the deep copy
    print("\nDeep copy:")
    print(deep_copy.__dict__)

    # Show the difference between the copies
    print("\nResults:")
    print("Original courses:", original.courses)
    print("Shallow copy courses:", shallow_copy.courses)
    print("Deep copy courses:", deep_copy.courses)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    print("\n=== Parent Object ===")
    parent = ParentClass("John", 45)
    print(parent.display_info())

    # Create and test a child object
    print("\n=== Child Object ===")
    child = ChildClass(
        "Jane",
        20,
        "S102",
        "Computer Science"
    )

    child.enroll_course("Python Programming")
    child.enroll_course("Database Systems")

    print(child.display_info())

    # Demonstrate inheritance
    print("\nInherited class variable:", child.category)

    # Demonstrate namespaces
    demonstrate_namespaces()

    # Demonstrate shallow and deep copying
    demonstrate_copying()


if __name__ == "__main__":
    main()