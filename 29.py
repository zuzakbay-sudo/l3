import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Input
r = int(input())

# Create Circle object
circle = Circle(r)

# Calculate area
area = circle.area()

# Output formatted to 2 decimal places
print(f"{area:.2f}")
