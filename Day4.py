#control structures-->if,elif,else..
#for(collection/range),while...

#write a program to generate the pattern of Right angled triangle


#Repetition part
'''print(2*3)
print('2'*4)

for i in range(8):
    #print(i,end='')
    print('*'*i)'''
    
    
#nested loops-->one another inside another for in side for..
#while inside while...

for i in range(1,3):
    for j in range(1,3):
        print(f'i={i},j={j}')

for i in range(1,6):
    for j in range(1,i+1):
        print(f'i={i},j={j}')



#below scenario also gives pattern of right angled triangl with better look

'''for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print('python')'''

#Write a program to generate table pattern from 1 to 5
'''for i in range(1,6):
    for j in range(1,11):
        #print(i*j)

for i in range(1,6):
    for j in range(1,11):
        print(i*j,end='') #print('i*j',end='')
    print()


for i in range(1,6):
    for j in range(1,11):
        print(i*j,end='\t')#'\t'-->tab space
     print()'''
#while -->only on test condition
#when we don't know end point we reply only on test expression
'''
while<test_expression>:
    statement(s)....
    .....

#print 1 to 10 numbers
for i in range(1,11):
    print(i)
    

i=1
while i<=10:
    print(i)
    i=i+1 #counter variable


a=[1,5,8,3]
d=0#output variable
for i in a:
    d=d+i
    print(d)
i=0#counter variable
while i<len(a):
    #print(i)
    #print(i,a[i])
    d=d+a[i]#indexing
    i=i+1
    print(d)

#write a program to print the below  pattern
rows=int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(i+1):
         print(j+1,end='')#i+j is floied 
    print()

#A program to print inverted pyramid pattern
rows=int(input("Enter:"))
for i in range(rows,0,-1):
    print()

rows=int(input("Enter:"))
for i in range(rows,0,-1):#reverse
    print('*'*i)  

rows=int(input("Enter:"))
for i in range(rows,0,-1):
    print('*',end='')
print()'''

#python-->Procedure Oriented+Object Oriented
#functins-->A block  of code that performs
#a specific task
#Syntax for Function:
'''
def fname(args): #function def #args=arguments
    """doc string(description of fn)"""
    statement(s)....
    ....
    return value(s)...
    print(fname(args))#function call

#create a function to perform sum of two integers
def add(a,b):
 """sample demo"""
 return a+b
print(add(21,31))
print(add('jeeva','mani'))
print(add([1,2,3],[4,5,6]))
#create an airthmatic function which takes 3 args as a,b,c performs
#addtn,multiplication,division,power

def arth(a,b,c):
 """Arthetic Function"""
 return a+b+c,a-b-c,a*b*c,a/b/c,a**2,b**2,c**2
print(arth(1,2,3))
d,e,f=map(int,input("enter:").split(','))
print(arth(d,e,f))

n=int(input("Enter a value"))
def fact(n):
    d=1#output variable
    for i in range(1,n+1):
          d=d*i#d*=i
          return d
        print(fact(n))

n=int(input("Enter a value"))
d=1#output variable
for i in range(1,n+1):
      d=d*i#d*=i
      print(d)'''













































































































    
    


























        
