"""
    Custom vector class
    its extended in global_settings.py
"""

# custom vector class
class Vector:

    def __init__(self, tuple: tuple[int, int]) -> None:
        self.x = tuple[0]
        self.y = tuple[1]

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_tuple(self) -> tuple[int,int]:
        return (self.x, self.y)

    # operator overloading
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y)

    def __mul__(self, o: int): # multiply vector and constant
        return Vector(self.x * o, self.y * o)
    
    def __mul__(self, o): # multiply vector and vector
        if isinstance(o, Vector):
            return Vector(self.x * o.x, self.y * o.y)
        else:
            raise TypeError("Both operands of '*' must be of type Vector or int")
    
    def __floordiv__(self, o: int): # divide vector by constant
        return Vector(self.x // o, self.y // o)

    def __truediv__(self, o):
        if isinstance(o, Vector):
            return Vector(self.x / o.x, self.y / o.y)
        else:
            raise TypeError("Right operand of '/' must be of type int or Vector")

Vector.ZERO = Vector(0, 0)
Vector.UP = Vector(0, -1)
Vector.DOWN = Vector(0, 1)
Vector.LEFT = Vector(-1, 0)
Vector.RIGHT = Vector(1, 0)