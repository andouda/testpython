class Animal:
    name='ポチ'
    age=10

    def __init__(self,n,a):
        self.name=n
        self.age=a

    def printAnimal(self):
        print(self.name,'は',self.age,'才です')

class Cat(Animal):
    pass

class Dog(Animal):
    pass

ani1=Cat('クロ',5)
ani2=Dog('太郎',10)

ani1.printAnimal()
ani2.printAnimal()