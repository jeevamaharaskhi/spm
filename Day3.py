'''
how do you define variables and datatypes and operators
Variables---->datatypes----->operators------->
control Structures'''
#operators
#Relational Operrators,Assignment Operators
#Membership Operators,Logical Operators

#Arthimatic Operators
#+,-,*,/(Floting division),//(Integer Division),%(Modulus),**(Exponent)
'''a=15;b=2
print(a/b)
print(a//b)#it returns quotient
print(a%b)#it returns remainder 
print(a**b)

#BODMAS/PEMDAS

print((a+b)-12*3)
#associativty principle only for
#Exponent operator is Right to left
print(2**3**2)'''

#Relational operators/comparission operators
#outcome is always boolean(True/False)
#==,!=,<,<=,>,>=
'''a=10;b=3
print(a==b)
print('code'!='python')

a=[1,4,5,8]
b=[1,5,8]
print(len(a)<len(b))
print('code'>'python')#checks alphabetical order'''

#Assignment Operators-->we assign the values-->=,+=,-=,*=...
'''a=5
#print(a)
#a=e # it should be e=a
e=a
#print(a)
#print(e==a)

#Update the values
a=a+5#a+=5
print(a)
b=3
b+=a
print(b)
c=5;d=4
c*=d#c=c*d
print(c)''' 

#Membershop Operators-checks for the
#existance in the sequence (collections)
#in,not in
'''print(5 in [1,2,5,8,9])
print('dog' not in 'dogs')
print(15 in {1:5,'name':'code',3:15})
#as 15 is not key'''

#Logical Operators-->and,or,not
#and-->all conditions to be satisfied
#or-->any one condition
#not-->
'''a=15;b=3;c=[1,2,4,5,15]
print(a>b and a in c) 
print(12==3 or a in c)#any one condition satisfied'''

#Control structures
#programmers/users want to repeat certain cases with revelant conditions
#Two  types
#1)Conditional Statements-->if,else,elif
#2)Repetition Statements(loops)
#for,while


#conditinal Statements-->
#Syntax for if
'''
if<test_expression>:
  Statement(s)..
  .....
'''
#a=5;b=3
'''a=int(input("Enter a value:"))
b=int(input("enter:"))
#print(a<b)
if a<b:
    a=a**2
    print(a)
if a>b:
    a=a**2
    print(a)
    
#so let's include with else block...
'''
'''else:
Statement(s)...
....
'''
'''if a<b:
    a=a**2
    print(a)
else:
    a=a+5
    print(a)'''

#Write a program to check whether
#a given number is even or odd

'''a=int(input("Enter a number:"))
if a%2:
    print("Even")
else:
    print("odd")'''

'''a=int(input("Enter a number:"))
if a%2==0:
    print("Even")
else:
    print("odd")

#Including more specific case
if a>0 and a%2==0:
    print("Even")
elif a<0:
    print("Negative Number")
else:
    print("odd")'''

#write a program to check whether he/she
#is eligible to vote or not in india
'''age=int(input("Enter the age:"))
if age>=18:
        print("He/She is eligible to vote")
else:
   # d=18-age
   #print("Not eligible",d,"years to wait")
   #print("He/She should wait for",18-age,"yrs to vote")        
   print(f'He/She should wait {18-age} years')'''

#keep a note to use if...elif...else...
#we want to repeat for certain number of cases
#loops->for,while
'''
syntax for:

for loop_varible in collection/range:
    statement(s)...
'''
'''a=[1,2,3,5,8]
#print(a[1
])#indexing
for i in a:
    #print(i)
    #print(i,i**2)
    print(i,end='')#use end='' or end='\t'''
    
'''a=['codegnan','jeeva','python']
#output-->
#b=['COEDGNAN','JEEVA','PYTHON']
b=[]#create an empty list
for i in a:
    #print(i,i.upper())
    b.append(i.upper())
    print(b)

b=['raskhi','jeeva','maha']
a=[]
for i in b:
   a.append(i.upper())
   print(a)'''

#Accepting,multiple inputs from user
'''names=input("Enter the data:").split(',')
print(names)'''

#To accept mulitiple integers from user
'''a=list(map(int,input("Enter:").split(',')))
print(a)
print(len(a))
                                         
a=set(map(int,input("Enter:").split(',')))
print(a)
print(len(a))'''

#write aprogram to find the sum of numbers in the list
'''a=[1,8,5,2,6,-3]
d=0#output varible for sum
for i in a:
    #print(i)
    d=d+i#d+=i
    print(d)
print(f'Sum is {d}')

data={'name':'codegnan',
      'place':'vjwda'}
for i in data:
    print(i)#it returns key only
    print(data[i])#it returns values

#range(stop)
#range(start,stop,step)
a=list(range(10))
print(a)

b=list(range(1,21,2))              
print(b)



for i in range(1,11):
    #print(i,end='')

#print numbers in reverse order from -20 to -1
for i in range(-20,0):
    print(i,end='')

#write a program to find sum of first 20 even numbers'''
d=0
'''for i in range(0,41):
    if i%2==0:
        #print(i,end='')
        d=d+i
        #print(d)
print(f'Sum of even numbers is {d}')
'''      
for i in range(0,41,2): #second way
    #print(i,end='')
        d=d+i
        #print(d)
print(f'Sum of even numbers is {d}')






