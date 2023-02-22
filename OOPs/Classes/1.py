class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f"Hi {self.name} How are you?")
        


bhumika=Person("Bhumika")
bhumika.talk();

