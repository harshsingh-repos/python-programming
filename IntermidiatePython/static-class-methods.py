#static and class methods

class Person(object):
    population = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def checkAdult(self):
        return self.isAdult(self.age)

    @classmethod
    def setPopulation(cls, new_population):
        cls.population = new_population

    @classmethod
    def getPopulation(cls):
        return (cls.population, cls.isAdult(18))

    @staticmethod
    def isAdult(age):
        return age >=18
    
    def display(self):
        print(self.name, "is of age : " , self.age)
        

person = Person("harsh", 34)

print(Person.getPopulation())
Person.setPopulation(200)
print(Person.getPopulation())

print(Person.isAdult(20))
person.display()