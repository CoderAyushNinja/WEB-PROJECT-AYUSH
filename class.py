class Exp1:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    
    def exp(self):
        x=1
        for i in range(self.num2,0,-1):
            x = x * self.num1
        return x
    def disp(self):
        print("The exponent of {} and {} is {}".format(self.num1,self.num2,self.exp()))

a=Exp1(4,3)
a.disp()
