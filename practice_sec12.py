###section12-1
##class Apple:
##    def __init__(self, w, c, v, p):
##        """weight[g]"""
##        self.weight = w
##        self.color = c
##        self.variety = v
##        self.producingarea = p
##        print("Created!")
##
##ap1 = Apple(280, "red", "紅玉", "Aomori")
##ap2 = Apple(295, "apple green", "Shinano Gold", "Nagano")
##print(ap1.variety)
##print(ap2.variety)
##
##
###section12-2
##import math
##
##class Circle:
##    def __init__(self, r):
##        self.radius = r
##        
##    def area(self):
##        return math.pow(self.radius, 2) * math.pi
##
##c1 = Circle(2)
##print(c1.area())
##        
##
###section12-3
##class Triangle:
##    def __init__(self, w, h):
##        self.width = w
##        self.height = h
##
##    def area(self):
##        return self.width * self.height * (1/2)
##
##t1 = Triangle(4, 3)
##print(t1.area())
##
##
#section12-4
class Hexagon:
    def __init__(self, len1, len2, len3, len4, len5, len6):
        self.length1 = len1
        self.length2 = len2
        self.length3 = len3
        self.length4 = len4
        self.length5 = len5
        self.length6 = len6

    def calculate_perimeter(self):
        return self.length1 + self.length2 + self.length3 + self.length4 + self.length5 + self.length6

h1 = Hexagon(1, 1, 3, 3, 5, 5)
print(h1.calculate_perimeter())

