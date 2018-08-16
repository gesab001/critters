class Dog():
    age = 0
    name = ""
    weight = 0

rambo = Dog()

class Person():
    name =""
    cellPhone = ""
    email = ""

giovanni = Person()
abigail = Person()
giovanni.name = "giovanni"
giovanni.cellPhone = "0273637989"
giovanni.email = "144000giovanni@gmail.com"

giovanni.name = "abigail"
giovanni.cellPhone = "0273637985"
giovanni.email = "aby318@gmail.com"

class Bird():
    color = ""
    name = ""
    breed = ""

class Mario():
    position = ""
    name = ""
    strength = ""

class Person():
    name = ""
    money = 0

nancy = Person()
nancy.name = "Nancy"
nancy.money = 100

bob = Person()
bob.name = "Bob"
bob.money = 50

print(bob.name, "has", bob.money, "dollars.")

class Animal():
    name = ""
    def eat(self):
        print ("munch munch")
    def makeNoise(self):
        print ("Grrrs says " + self.name)
    def __init__(self):
        self.born = "An animal has been born"
        print(self.born)

class Cat(Animal):
    def makeNoise(self):
        print ("meow " + "says " + self.name)
    def __init__(self):
        self.born = "A cat has been born"
        print(self.born)


class Dog(Animal):
    def makeNoise(self):
        print ("Bark " + "says " + self.name)

    def __init__(self):
        self.born = "A dog has been born"
        print (self.born)

print()
cat = Cat()
cat.name = "Kitty"
cat.makeNoise()
cat.eat()
print()

dog1 = Dog()
dog1.name = "Rambo"
dog1.makeNoise()
dog1.eat()
print()

dog2 = Dog()
dog2.name = "Silver"
dog2.makeNoise()
dog2.eat()
print()

giraffe = Animal()
giraffe.name = "Mark"
giraffe.makeNoise()
giraffe.eat()