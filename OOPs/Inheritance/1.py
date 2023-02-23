class Mammals:    #parent class
    def use(self):
        print("walk")
    
class Dog(Mammals):  #inherited class
    def bark(self):
        print("bark")
    
class Cat(Mammals):
    pass            #used to pass empty class when we dont wnat to write anything to avoid error


dog1 = Dog()
dog1.use()     #dog1 inherited from mammals
dog1.bark()
cat1 = Mammals()  #cat 1 interited from mammals
cat1.use()
