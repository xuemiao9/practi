
#import add from comm
#from comm.calculatorfile import add
from comm import calculatorfile

class Test :
    t = 0
    __p = 0
    def __init__(self,name):
        self.name1=name;
        #Test.t+=1
        self.t+=1
        Test.__p += 1

    def display(self):
        print "name="+self.name1 +",t=%d"%Test.t
        print "name="+self.name1 +",t=%d" % self.t

t1=Test("1test")
t1.display()
print Test.t
print t1.t
Test.t+=1
t2=Test("2test")
t2.display()
print Test.t
print t2.t
#print t2.__p

try:
    print t2.__p
except AttributeError:
    print "error"
finally:
    print t2._Test__p
print t2.__dict__

a1=calculatorfile.add(1,2)
print a1.ext()