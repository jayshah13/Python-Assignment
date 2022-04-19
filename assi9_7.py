class P1_class(): 

    def show(self): 
        print("Inside Parent Class 1") 


class P2_class():
    def display(self): 
        print("Inside Parent Class 2")


class C1_class(P1_class, P2_class):
    def show(self): 
        print("Inside Child Class 1")


obj = C1_class() 

obj.show()  

obj.display() 