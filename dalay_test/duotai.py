class Animal():
    def eat(self):
        print('eat food')

    def talk(self):
        print('makenoise')

    def run(self):
        print('running')


class Dog(Animal):
    def eat(self):
        print('dog eat')

    def talk(self):
        print('Dog w w w')

    def run(self):
        print('Dog runing')

class Pig(Animal):
    def eat(self):
        print('Pig eat')

    def talk(self):
        print('Pig heng heng ')

    def run(self):
        print('Pig runing')


def use_animal(animal):
    animal.eat()
    animal.talk()
    animal.run()

d1 = Dog()
p1 = Pig()
use_animal(d1)
use_animal(p1)
