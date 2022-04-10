
class Mammal:
    def walk(self):
        print("walk")
    def color(self):
        print("black")

class Dog(Mammal):
    def bark(self):
        print('bark')

class Cat(Mammal):
    def mew(self):
        print('Mew')


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.color()