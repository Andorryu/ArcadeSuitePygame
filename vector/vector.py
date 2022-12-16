"""
    Custom vector class
    its extended in global_settings.py
"""

# custom vector class
class Vector:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, tuple: tuple[int, int]) -> None:
        return cls(tuple[0], tuple[1])

    def copy(self):
        return Vector(self.x, self.y)

    def as_tuple(self) -> tuple[int,int]:
        return ((self.x, self.y))

    # operator overloading
    def __add__(self, o):
        if isinstance(o, Vector):
            return Vector(self.x + o.x, self.y + o.y)
        elif isinstance(o, int):
            return Vector(self.x + o, self.y + o)
        else:
            raise TypeError("Both operands of '+' must be of type Vector or int")

    def __sub__(self, o):
        if isinstance(o, Vector):
            return Vector(self.x - o.x, self.y - o.y)
        elif isinstance(o, int):
            return Vector(self.x - o, self.y - o)
        else:
            raise TypeError("Both operands of '-' must be of type Vector or int")
    
    def __mul__(self, o): # multiply vector and vector
        if isinstance(o, Vector):
            return Vector(self.x * o.x, self.y * o.y)
        elif isinstance(o, int):
            return Vector(self.x * o, self.y * o)
        else:
            raise TypeError("Both operands of '*' must be of type Vector or int")
    
    def __floordiv__(self, o): # divide vector by constant
        if isinstance(o, int):
            return Vector(self.x // o, self.y // o)
        if isinstance(o, Vector):
            return Vector(self.x // o.x, self.y // o.y)

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
