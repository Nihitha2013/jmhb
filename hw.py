import math

class circle:
    def __init__(self,radius):
       self.radius=radius
    
    def area(self):
        return math.pi *(self.radius**2)
    
    def perimeter(self):
        return 2*math.pi* self.radius
    
a=float(input("Enter the radius:"))
Circle=circle(a)
print("Area:",Circle.area())
print("Perimeter:", Circle.perimeter())