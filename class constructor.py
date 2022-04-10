
class Point:
    # class constructor, __init__ stands for initialization
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)
print(point.y)
point.x = 2
print(point.x)