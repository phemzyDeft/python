
# Pascal naming convention
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# an object is an instance of a class
point1 = Point()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)
point1.draw()

point2 = Point()
point2.x = 50
print(point2.x)


