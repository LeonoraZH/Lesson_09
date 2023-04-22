# реализовать метакласс. позволяющий создавать всегда один и тот же объект класса

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    def __init__(self, name):
        self.name = name
