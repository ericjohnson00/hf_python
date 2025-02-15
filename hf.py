"""help() function for Python objects"""

class Car:
    """Car class"""
    def __init__(self, make, model):
        self.make = make
        self.model = model

help(Car)


print(dir(Car))