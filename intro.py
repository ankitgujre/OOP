'''
What is OOP?
OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and 
objects for better organization and reusability.
'''

'''
Advantages of OOP
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code
Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated 
code into functions or classes and reuse it.

What are Classes and Objects?
Classes and objects are the two core concepts in object-oriented programming.

A class defines what an object should look like, and an object is created based on that class
'''

'''
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
'''

# Create a class named MyClass, with a property named x:

class MyClass:
    x = 5
    
# Now we can use the class named MyClass to create objects:

# Example
# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
print(type(p1.x))