class Jets:
    model = None
    country = 0
    
    def __init__(self,name,country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country
        
    def display(self):
        print(f"\nDisplaying name and country in Jets class : {self.name},{self.origin}")
        
class F14(Jets):
    
    def __init__(self):
        super().__init__("F14","USA")
        self.engine = 2
        self.seat = 2
        self.tail = 2
        print(f"\nDisplaying name and country  in F14 class : {self.name},{self.origin}")
        
    def engine_method(self):
        print(f"\nTotal Engines in F14 fighter jet is {self.engine}")
        
    def seat_method(self):
        print(f"\nTotal seats in F14 fighter jet is {self.seat}")
        
    def speed_method(self,speed : int):
        self.speed = speed
        print(f"\nThe speed of the  F14 fighter jet is {self.speed} miles per hour")
        
    def tail_method(self):
        print(f"\nTotal tails in F14 fighter jet is {self.tail}")
        
obj2 = Jets("Air India","India")
        
obj1 = F14()

obj2.display()

obj1.engine_method()
obj1.tail_method()
obj1.speed_method(200)
obj1.seat_method()

