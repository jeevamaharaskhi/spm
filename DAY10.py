#Built-in Functiond-->60+as of 3.x version
#print(dir(__builtins__))
#Every built-in datatype is a built in function
#int(),float(),c0mplex(),str(),list(),tuple(),set(),dict()
'''a="codegnan"
#convert to dict
b=dict.fromkeys(a)
#print(b)
#print(len(b))
#print(type(a))

#print(min(b))#check the keys
#print(max(b))


#any(),all(),sorted(),reversed(),zip(),enumerate()

#any(iterable)-->checks for atlest one object

a=[1,2,'',[],25,3.2]
#print(len(a))
#print(any(a))
#print(all(a))

a=(12,8,12,3,-5,6.3)
#sort the tuple
b=list(a)
#print(b)
b.sort()
#print(b)

c=sorted(a)
#print(c) #or

#print(sorted(a))

#decending order
d=sorted(a,reverse=True)
#print(d)#or

#print(sorted(a,reverse=True))

#zip(),enumerate()

#zip(*iterables)-->converts multiple collections into a single iterable

a=[1,5,8,9,12];b=[1,8,5,12]
c=list(zip(a,b))
#print(c)


data=[121,125,135,128]
names=['code','parker','tony','steve']
new=dict(zip(data,names))
#print(new)

#enumerate()-->provides a default counter object for given collection
names=['python','java','codegnan']
c=dict(enumerate(names))#default is 0
print(c)

d=dict(enumerate(names,1))
print(d)

for i,j in enumerate(names):#optimized approch
    #print(i,j)
    print(f'{i}:{j}')
    
for i in range(len(names)):#general approch
    print(f'{i}:{names[i]}')


#print(pow(5,3))
#print(5**3)

a=75.64
#print(round(a))
#print(round(a,2))

a=[1,5,8,12,-3,5]
#print(sum(a))#sum of given collection

#print(sum(range(11)))#sum of first 10 numbers

#print(sum(range(1,21,2)))#sum of odd numbers

#Anonymous Functions(lambda keyword)
#these are generally temporay functions and
#even they can be used as arguments for some
#built-in functions-->filter(),map()

#syntax for anonymous functions

#lambda arg(s):expression

#user defind vs lambda

#write a Mathematical function with eqn 3*x+5
#when x=5

def f(x):
    return 3*x+5
print(f(5))

#same above functionas lambda function
d=lambda x:3*x+5 #anonymous fun
print(type(d))
print(d(5))

'''


#e=lambda x,y:x**y
#print(e(5,2))


#f=lambda fname,lname:fname+lname
#print(f"Rakshitha","Darnasi")


#f=lambda fname,lname:fname.title()+" "+lname.title()
#full_name=f("rakshitha","darnasi")
#print(full_name)

#filter()-->returns a new collection after perform reqd logic

#a=[int(x)for x in input("Enter:").split(',')]
#print(a)
#filter only even numbers from above list
#b=list(filter(lambda i:i%2==0,a))
#print(b)

#map-->maps every objects to form a new collection


#a=list(map(int,input("Enter:").split(',')))
#print(a)


#a,b,c=map(int,input("Enter:").split(','))
#print(a,b,c,a+b+c)

a=[1,2,5,8,25];b=[1,4,5,6]
#c=list(map(lambda i,j:i+j,a,b))
#print(c)


#keep a practice on user defines,built-in and lambda usage

#Procedure oriented->Above functions usage
#__main__()-->import-->Module
#Object Otiented paradigm-->class,object

'''
A class contains attributes/methods that can manipulate the data

A class is generic in nature whereas object is specific in nature

Parrots,Pigeon,Sparrow-->birds class

A class is the blueprint of an object

Remember an example prepares dimensions(l,b,h)-->class
wood->memory

syntax:

class ClassName:
 """docstring"""
 attributes means variable...
 x=5
 y=10#sample
 #methods(funtions inside class)
 def sample(self):
     self.x=x
     self.y=y
#create an object
a=ClassName()


#Simple class declaration and object creation

class Person:
    """Simple person class to store details"""
    name="RakshiJeeva"
    place="Heaven"
    #create a method to access above variables
    def details(self):
        print(f'{self.name} belongs to {self.place}')
#creation of object
p=Person()
#print(dir(p))
print(p.name)
print(p.place)
p.details()


class Person:
    """Simple person class to store details"""
    #Create a method to store details
    #self is like a reference which carries all
    #attribute/methods for an object
    def storing(self,name,place):
        self.name=name
        self.place=place
    #create a method to access above variables
    def details(self):
        print(f'{self.name} is in {self.place}')
#create an object
a=Person()
#print(dir(a))
#a.details()
a.storing('Rakshi','A.M.Reddy')
print(dir(a))
a.details()

#we can create any no.of objects
b=Person()
b.storing('Rakshi','pdrl')
b.details()

#Accepting user inputs
class Person:
    """Simple person class to store details"""
    #Create a method to store details
    #self is like a reference which carries all
    #attribute/methods for an object
    def storing(self):
        self.name=input("Enter the name:")
        self.place=input("Enter the place:")
        self.age=int(input("Enter the age:"))
    #create a method to access above variables
    def details(self):
        print(f'{self.name} is in {self.place} is {self.age} years old')
a=Person()#first object
a.storing()
a.details()
print(a.__dict__)#namespace of part.object
b=Person()#second oject
b.storing()
b.details()
'''
#constructor (__init__())
class Person:
    """Simple person class to store details"""
    #Create a method to store details
    #self is like a reference which carries all
    #attribute/methods for an object
    #def storing(self):
    def __init__(self):#object initialization
        self.name="sara"
        self.place="Gnt"
        self.age=3
    #create a method to access above variables
    def details(self):
        print(f'{self.name} studying in {self.place} from {self.age} years')
a=Person()
a.details()

class Person:
    """Simple person class to store details"""
    #Create a method to store details
    #self is like a reference which carries all
    #attribute/methods for an object
    #def storing(self):
    def __init__(self,age,name,place):#object initialization
        self.x=name
        self.y=place
        self.z=age
    #create a method to access above variables
    def details(self):
        print(f'{self.x} studing in {self.y} from {self.z} years')
a=Person(3,"Rakhsi","AMRN")
a.details()

























