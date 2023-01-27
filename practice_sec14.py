#section14-1
class Square:
    square_list = []

    def __init__(self, l):
        self.lengths = l
        self.square_list.append(self.lengths)
        
    def calculate_perimeter(self):
        self.perim = 0
        for l in self.lengths:
            self.perim = self.perim + l
        self.square_list.append(self.perim)
        return self.perim
    

#section14-2
    def print_size(self):
        print("{} by {} by {} by {}".format(self.lengths[0], self.lengths[1], self.lengths[2], self.lengths[3]))


squ1 = Square([1, 4, 2, 3])
print(squ1.calculate_perimeter())
print(squ1.square_list)
squ1.print_size()


#section14-3
class Person:
    def __init__(self):
        self.name = 'Bob'

def same_another(name1, name2):
    print(name1 is name2)

bob = Person()

same_bob = bob
same_another(bob, same_bob)

another_bob = Person()
same_another(bob, another_bob)

