class Dog(object):
    def __init__(self,name):
        self.name = name

class FlyDog(Dog):
    pass

class Person(object):
    def __init__(self,name):
        self.name = name

    def play_game_with_dog(self,dog):
        print(f'{self.name} is playing with {dog.name}')

d1 = Dog('dog')
f1 = FlyDog('flydog')
p1 =Person('pangu')

p1.play_game_with_dog(d1)
p1.play_game_with_dog(f1)

