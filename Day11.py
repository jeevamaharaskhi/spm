'''
Usage/Importance of Underscore in python
->Single Underscore-->'_'
->Single Trailing underscore->'var_'
-->double leading underscore-->'__var'
-->double leading and double training underscores
(python special methods-->__var__)


#Single Underscor:Itis generally used for
#temporary pirposes/to join multiple words
#snake case conventin

for _ in range(1,11):
    print(_,end='')

email_id="jeevamanibejjipalli@gmail.com"
print(email_id)
mobile_no=9392614493
print(mobile_no)


#single trailing underscore-->var_
#it is generally used in order to avoid name
#conflicts with python keywords

def student(name,age,class_):
    print(f'{name} is of {age} years old in {class_} class')
student("JEEVAMANI",21,15)
'''
#Double leading underscore-->__var
'''
Whenever we denote double leading underscores before a variable
name/identifier,python interpreter treats as a private variable,
it rewrites the names in orderto avoid name clases with inner methods

class Details:
    """Usage of double leading underscore"""
    def __init__(self):
        self.name="JEEVAMANI"
        self._place="TNK"
        self.__age=21
a=Details()
print(dir(a))
#print(f'{a.name} is in {a._place} of {a.__age} old')
print(f'{a.name} is in {a._place} of {a._Details__age} yers old')

#Double leading and Double trailing underscores these are epresents
#Which python follows for special methods

class Students:
    """Student class with basic details"""
   #def details(self):
    def __init__(self):#replace your method name with constructor
        self.name="JEEVAMANI"
        self.place="TNK"
        self.branch="CSE"
#a=Students()#create the object
#a.details()#then refer/acces the method
#print(a.name)
a=Students()
print(a.name,"is in",a.place)
print(a.__dict__)#namespace


#we  pronounce as dunders(double underscore)
a=5;b=3
print(a+b)

print(a.__add__(25))
print(a.__divmod__(b))#5//3-->1,5%3-->2
print(a.__ge__(b))

a=[1,5,8,9,6]#always check type first
print(len(a))

print(a.__getitem__(2))#a[2]

#Those Special Methods for any object are term as magic mrthods


#create a student class to accept marks and other details as input
#and evaluate the grades
#We will use__init__()for object initilaization

class Students:
    """Students class with Construstor"""
    def __init__(self,name="abc",marks=100):
        self.name=name
        self.marks=marks
        #Instance methods
    def display(self):
            print(f'Student name is {self.name}')
            print(f'He/She got {self.marks} marks')
#a=Students()#default attributes
#a.display()
#b=Students("JEEVAMANI",250)
#b.display
  #Instance method to evaluate grades
    def evaluate(self):
         if self.marks>=700:
             print(f'He/She secured First grade')
         elif self.marks>=500:
             print(f'He/She secured second grade')
         else:
            print(f'Sorry you failed prepare well')
#a=Students()
#a.display()
#a.evaluate()
#let's make it dynamic to accept n numbeqr
qn=int(input("Enter the number of students:"))
for i in range(n):
    x=input("Enter the student name:")
    y=int(input("Enter the marks:"))
    a=Students(x,y)
    a.display()
    a.evaluate()
    print('--------------------------------------')


#A function is like a House where as class is like a Power House

#Exception handlig
#Errors that occur during exception can be handled by try,except statements
#with finally keyword

#Errors-->Runtime Errors,logical Errors,Syntax Errors

#Syntax Errors-->Invalid syntax,Indentation,mis match braces....
#Learner should avoid them

#Runtime Error->ValueErrors,IndexErrors,
#TypeError,Attribute Errors...-->try,except will be closed by finally block

#LogicalErors and Syntax Errors are to be handled by programmers/Users

#Every try block must have one hour more except blocks

#Simple usecase for try-except block with assert(keyword) usage
#a,b=map(int,input("Enter the values:").split(','))
#print(a,b)
#Usage of assert
#Syntaax for assert-->expression,message
#assert a>0
#assert a>0,"Enter only +ve numbers"
#print(a**b)

#As in above case we made message along with AssertinError let's handle it

try:
    a,b=map(int,input("Enter the values:").split(','))
    print(a,b)
    assert a>0,"Enter only +ve numbers"
    print(a**b)
#except:
    #print("Wrong input")
except Exception as e:#message for errors
    print(e)
'''

#Now we will write individual except blocks
try:
    a,b=map(int,input("Enter the values:").split(','))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Enter Denominator other than zero")
except ValueError:
    print("Flot/Str cannot be taken")
except Exception as e:
    print(e)
finally:
    print("Done")








































