'''a=31
b=21
print(a+b)
a=5
print(type(a))
i3=2
b=5+i3
print(b)
c=5+3j
print(c)
print(type(c))
a=90
print(type(a))
b=float(a)
print(b)
c=complex(a)
print(c)'''
'''a=30.5
print(type(a))
b=complex(a)
print(b)
c=int(a)
print(c)'''

'''a=5+2.3+(52+3j)+True
#print(a)
a="daughterofgod"
#print(a)
#print(type(a))
#print(len(a))
#print(a[0])
#print(a[7])
a="12356"
#print(len(a))
b='jeeva mani bejjipalli'
#print(b[-1])
#print(len(b))
#print(b[2])
c=b[2]+b[-3]+b[5]
#print(c)
#print(b[5:])
#print(b[5:10])
#print(b[-3:-10])#empty
#print(b[-10:-3])
#print(b[3:-10])
#print(b[-10:3])
a="jeeva jeevamani"
#print(a[3:])
#a[3:]="python" #strings are immutable

#string-->ArithmeticError[start:end:step]
#print(a[1:5:0]) #step cannot be zero
#print(a[1:5:2])
#print(a[1:5:1])
#print(a[:8:3]) #a[0:8-->'jeeva jee'-->jvj(step 2)
#print(a[::-1])
#print(a[::-2])#alternate character in reverse order


#Functions-->case converrsions,joing,splitting
#Concatenation
a="daughter of god"
#upper(),lower(),title(),capitalize()
#print(a.upper())#converts to uppercase
b=a.upper()
#print(b)
c=a.lower()
#print(c)
d=a.title()
#print(d)
f=a.capitalize()
#print(f)


#isupper(),islower(),isalpha(),isalnum(),isdigit()
#output returns boolen-->True/False

#print(a.isupper())
#print(a.islower())
#print(a.isalpha())#space also a character
#print(a.isdigit())
#print('code123'.isalpha())
#print('code123'.isalnum())
#print('12345'.isalnum())'''


'''#count(),index(),find(),split()
a="daughter of god is wonderful"
print(a.count('o'))
#print(a.count('n'))#it not present-->0

#index()-->returns only first occurence
print(a.index('o'))
print(a.rindex('o'))#returns last occurance

print(a.index('o',3))
print(a.index('o',9))
print(a.index('o',20))

a='jeeva'
#print(a.index('m'))#returns value error

#find()-->overrides the error
print(a.find('e'))#returns first occurance
print(a.find('m'))#returns-1'''

#join(),split()

a="jeeva";b="mani"
c=a+b#string concatination
print(a+b)
 

d=a.join(b)#join(iterable)-->collection
print(d)


e="!".join("jeeva")
#print(e)

#split()-->divides according to given objects(list)
d=a.split()
print(d)
print('daughter of god'.split())#default split at space


















