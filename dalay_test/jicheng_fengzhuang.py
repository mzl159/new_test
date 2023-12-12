class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def talk(self):
        print(f'{self.name} is talking, he is {self.age}')

    def run(self):
        print(f'{self.name} is running')

    def change_age(self, new_age):
        self.age = new_age

    def reboot(self):
        for i in range(4):
            print(i)
        print('robot is running')


p1 = Person('sam', 19, '男')
p1.talk()
p1.change_age(29)
print(p1.age)
p1.run()
p1.reboot()

class NewPerson(Person):
    pass


p2 = NewPerson('jack',20,'男')
p2.run()


