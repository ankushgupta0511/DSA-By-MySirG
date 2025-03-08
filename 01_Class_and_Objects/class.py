# its comments
""" 
class Test:
    x=5   # this is a class variable if we declare inside __init__ F() then it is called instence variable
    def f1(self):
        print("Hellow")
t1=Test()
t1.f1()
t2=Test()
t2.f1()

"""



################################################################

""" 
class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
t1=Test(5,10)
t2=Test(20,25)
print(t1.a,t1.b)
print(t2.a,t2.b)

"""

################################


class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    
    def f1(self):  # class F()
        print(self.a,self.b)   
        pass
    @staticmethod   
    def f2():  # no need to give any arguments
        print("static method")

    @classmethod
    def f3(clg):  #  need to give any arguments and clg is a instance or object of class
        print('class method')
    
t1=Test(5,10)
t2=Test(20,25)
t1.f1()
Test.f2()
Test.f3()