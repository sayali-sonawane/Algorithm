from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name
        self._a = 2 # private - still accessible by outside class, but that's the convention
        self.__b = 3 # protected - to make it really not acessible outside the class

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    @abstractmethod
    def printStatement(self):
        print("I am abstracted.")

    def greatGatsby(self):
        print("I am not abstracted.")

class Student(Person):
    def getName(self):
        print("My name is", self.name)

    def printStatement(self):
        print("I am student abstracting abc.")

class Faculty(Person):
    # def __init__(self, name):
        # super().__init__("Faculty")
        # pass

    def getName(self):
        print("I am Prof.", self.name)

    def getA(self):
        print(self._a)

    def getB(self):
        print(self.__b)

    def printStatement(self):
        print("I am a faculty abstracting abc.")

class Cats:
    def __init__(self, name):
        self.name = name

    def getName(self):
        person = Person("Shandy")
        print(person._a)

stud = Student("Harsh")
fac = Faculty("Wollega")
cat = Cats("Spooky")
# person = Person("Hari")

# fac.getName()
# print(fac.__class__.__name__)
# print(fac)
# stud.getName()
# print(stud.__class__.__name__)

# fac.getA()
# fac.getB()

# print(person._a)

# cat.getName()

# fac.printStatement()
# stud.printStatement()
# person.printStatement()

# fac.greatGatsby()
# stud.greatGatsby()


from heapq import heappush, heapify, heappop

h = []
heappush(h, (1,3,'a'))
heappush(h, (3,5,'b'))
heappush(h, (3,4,'c'))
heappush(h, (1,2,'d'))
heappush(h, (2,3,'e'))

print(heappop(h)[2])
print(heappop(h)[2])
print(heappop(h)[2])
print(heappop(h)[2])
print(heappop(h)[2])
