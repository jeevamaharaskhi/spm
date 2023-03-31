#Funtions-->A group of statements that performs a specific given task
#Arguments in the function
#1)Positional Arguments
#2)Keyword Arguments
#3)Default Arguments
#4)Variable length arguments(*args)
#5)Keyword variable length arguments(**kwargs)
'''
#Number of arguments in function defn should match with function call

def data(a,b,c):
  """Postal arguments demo"""
  return a*b+c
print(data(15,2,3.5))
#print(data(15,3.5))#less number
#print(data(15,2,3.5,8))#more number 

#Keyword arguments-->we can define some names for the arguments

def college(name,branch):
    """keyword arguments demo"""
    print(f'name is {name}')
    print(f'studying in {branch}')
#college("jeeva","cse")
#college("cse","jeeva")
college(name="Jeevamani",
        branch="CSE")

#Default arguments
#we can make some arguments but not first argument as default


def Area(branch,college='amreddy'):
    """Default arguments demo"""
    print(f'He/She is in {branch} branch of {college} college')
Area("Agriculture")
Area("CSE")
Area(college="Eswar",branch="CSE")
Area(branch="ECE")
#Variable length arguments
#number of arguments are not fixed so we can use*representation,
#initially data is stored in tuple

#def check(args):
def check(*args):#to give more values
    print(args)
    print(type(args))
check()
check(5,8,12,3.2,'poll')
b=[1,2,3,44]
check(*b)#unpacks every object from list

#write a fun'n to find the sum of number by accepting from user

#a=list(map(int,input("Enter values:").split(',')))
#print(a)
#print(sum(a))
def add(*b):
    """args demo"""
    print(b)
    d=0#output variable
    for i in b:
        if type(i)==int or type(i)==float or type(i)==complex:
            d=d+i
            print(d)
#add(2,3,5.6)
#add(2,3,'J',5.6,2+3j,31)

a=list(map(int,input("Enter values:").split(',')))
print(a)
add(*a)# in list read step by step values can use add(*a)

#usage of *to unpack objects such as below
a,*b,c=[1,2,3,4,55,6]
print(a)
print(b)
print(c)

a,*b='codegnan'
#print(a,b)


a,*b=list(map(int,input("Enter values:").split(',')))
print(a)
print(b)

#keyword variable length arguments
#we can use keywords and arguments in any number
#by using ** representation
#it internally stores in dictionary

def new(**args):
    print(args)
    print(type(args))
#new()
#new(idno=502,name='Jeevamani',branch='CSE',college='Amreddy',mailid ='Jeevamani123@gmail.com')
data={'idnos':[501,502,507,547],
      'branch':['CSE','ECE','CS','CIVIL','AGRI','EEE','Mech'],
      'college':'AMRN'}
new(**data)

#Usage of both*args and **kwargs

def final(*a,**b):
    print(a)
    print(b)
    for i in b:
        print(i)
ids=[1,2,3,4,5]
#names=['code','made','pot','bat']
names={'branch':'CSE',
       'gender':['M','F']}
final(*ids,**names)
final(1,2,6,name='Jeeva',
      email='Jeevamani123@gmail.com',
      mob=9392614493)'''




#Module-->Every Python file is a Module
#we use keyword called as import

def check():
    if __name__=="__main__":
        print("This program is run as a script")
    else:
        print("This program is run as a Module")
#check()
print(__name__)

data={'name':'codegnan','place':'vjwda'}



 




    










































































































































































































 
