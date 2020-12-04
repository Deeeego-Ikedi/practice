#section13-1
class Rectangle:
    def __init__(self, l):
        """l:各辺の長さ"""
        self.lengths = l
        
    def calculate_perimeter(self):
        self.perim = 0
        for l in self.lengths:
            self.perim = self.perim + l
        return self.perim

rec1 = Rectangle([1, 1, 3, 3, 5, 5])
print(rec1.calculate_perimeter())

class Square:
    def __init__(self, l):
        self.lengths = l
        
    def calculate_perimeter(self):
        self.perim = 0
        for l in self.lengths:
            self.perim = self.perim + l
        return self.perim

#section13-2
    def change_size(self, index, l):
        self.lengths[index] = l   

squ1 = Square([1, 4, 2, 3])
print(squ1.calculate_perimeter())
squ2 = squ1
squ2.change_size(0, 2)
print(squ2.calculate_perimeter())


section13-3
class Shape:
    def __init__(self, l):
        self.lengths = l

    def what_am_i(self):
        return print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rec1 = Rectangle([1, 1, 3, 3, 5, 5])
print(rec1.what_am_i())
squ1 = Square([1, 4, 2, 3])
print(squ1.what_am_i())


#section13-4
class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

yutaka = Rider("Yutaka Take")
kb = Horse("Kitasan Black", "halo", yutaka)
print(kb.owner.name)
        


