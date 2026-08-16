from abc import ABC, abstractmethod

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Robot(Workable):
    def work(self):
        print("Robot is working")
    
class Worker(Workable,Eatable):
    
    def eat(self):
        print("Worker is eating")
    
    def work(self):
        print("Worker is working")

r = Robot()
r.work()
w = Worker()
w.work()
w.eat()