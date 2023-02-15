class Fraction:
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom  
        while self.num%self.den != 0:
          oldm = self.num
          oldn = self.den

          self.num = oldn
          self.den = oldm%oldn
   
    def show(self):
        print(self.num,'/',self.den)
    def __str__(self):
        return str(self.num)+'//'+str(self.den)

    def __eq__(self, other):
        firstmun = self.num * other.den
        secondnum = other.num * self.den
        return firstmun == secondnum

    def getNum(self):
        num = self.num
        return num
    def getDen(self):
        den = self.den
        return den    

myf = Fraction(2,4)

# myf.show()
# myf.__str__()

# myf1 = Fraction(1,3)
# myf2 = Fraction(1,3)
print(myf)

num = myf.getNum()
print(num)
den = myf.getDen()
print(den)