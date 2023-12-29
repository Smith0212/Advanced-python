class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator (+)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the subtraction operator (-)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overloading the multiplication operator (*)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Overloading the equality operator (==)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading the string representation of the object
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Testing the Vector class
if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    # Testing addition
    result_add = v1 + v2
    print(f"Addition: {result_add}")  # Output: Addition: Vector(4, 6)

    # Testing subtraction
    result_sub = v1 - v2
    print(f"Subtraction: {result_sub}")  # Output: Subtraction: Vector(-2, -2)

    # Testing multiplication
    scalar = 2
    result_mul = v1 * scalar
    print(f"Multiplication: {result_mul}")  # Output: Multiplication: Vector(2, 4)

    # Testing equality
    v3 = Vector(1, 2)
    print(f"Are v1 and v3 equal? {v1 == v3}")  # Output: Are v1 and v3 equal? True
