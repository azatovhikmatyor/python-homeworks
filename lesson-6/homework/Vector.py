import math

class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __bool__(self):
        return any(self.components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, index, value):
        self.components[index] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be of the same length for multiplication.")
            return Vector(*(a * b for a, b in zip(self.components, other.components)))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Unsupported operation for multiplication.")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return Vector(*(a / scalar for a in self.components))
        else:
            raise TypeError("Division only supports scalars (int or float).")

    def __eq__(self, other):
        return self.components == other.components

    def __neg__(self):
        return Vector(*(-a for a in self.components))

    def __abs__(self):
        return math.sqrt(sum(a ** 2 for a in self.components))


# Example Usage
v1 = Vector(1, 4, 6)
print(v1)                # Vector(1, 4, 6)
print(bool(v1))          # True
print(len(v1))           # 3
print(v1[1])             # 4
v1[1] = 10
print(v1)                # Vector(1, 10, 6)

v2 = Vector(3, 7, 2)
print(v1 + v2)           # Vector(4, 17, 8)
print(v1 - v2)           # Vector(-2, 3, 4)
print(v1 * v2)           # Vector(3, 70, 12)
print(v1 * 3)            # Vector(3, 30, 18)
print(v1 / 2)            # Vector(0.5, 5.0, 3.0)
print(abs(v1))           # 11.66...
print(v1 == Vector(1, 10, 6))  # True
print(-v1)               # Vector(-1, -10, -6)
