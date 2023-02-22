class Person:
    def __init__(self,name): #constructor
        self.name=name
        
    def talk(self):
        print(f"Hi {self.name} How are you?")  #formatted string
        


bhumika=Person("Bhumika")   #object belonging to person class
bhumika.talk();

