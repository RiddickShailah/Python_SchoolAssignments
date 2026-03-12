class Location:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __le__(self,other):
        return self.x <= other.x and self.y <= other.y

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

loc1= Location(3,4)
loc2 = Location(5,8)
print(loc1== loc2)
print (loc1<=loc2)