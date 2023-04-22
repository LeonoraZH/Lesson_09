# реализовать дескрипторы для любых двух классов

class Age:
    def __get__(self, instance, owner):
        return instance._age
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer.")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120.")
        instance._age = value

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    age = Age()
    
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
