#Lists-->a collection of same/diffrnt objects within []and it is Mutable

'''a=[1,2.3,'codegnan',2+3j]
print(a)
print(type(a))
print(len(a))
print(a[-2])#indexing
print(a[1:3])#slicing
print(len(a[2]))#it is possible only for collection
print(a[2][::-1])'''

#perform indexing,slicing,striding
'''a=[1,5,'python',20,2018]
print(a)
print(len(a))
a[1]=31#changing the elements
print(a)
#print(a[2:4])
a[2:4]=['jeeva,cse']
print(a)

#task-->
a=[1,5,'python',20,2008]
#output -->b=[12,5,'codegnan',20,2023]
a[0]=12;a[2]=['codegnan'];a[4]=[2023]
print(a)
#or
a[0]=12
a[2]=['codegnan']
a[-1]=2023
#or
print(a[0::2])
a[0::2]=[12,'codegnan',2023]
print(a)

#we loose orgnal data if we add elements using indexing,slicing,striding
b=[1,5,[12,3,'code'],26]
print(b)
print(len(b))
b[-2]=125
print(b)
b=[1,5,125,6]
# we use append(),extend(),insert()
b.append(256)#add single element last
print(b)
b.append([1,2])#nested list
print(b)

#extend(iterable)->adds group of objects
#to end of the list
b=[1,2,3,4]
print(b)
b.extend([1,2,5])
print(b)
#insert(index,object)-->adds element before index
b=[1,2,3]
b.insert(3,'jeeva')
print(b)
b.insert(2,['rakshi,maha'])
print(b)

#remove elements from the list
#pop(),remove(),clear()

a=[12,5,8,'am',123]
#pop()-->if we give index it removes accrdngly
#else Last in First Out
a.pop()
a.pop(1)#we give index as 1
print(a)

#remove(value)it removes only first occurance
a=[12,5,8,'am',123]
#a.extend('code')
#print(a)
#print(len(a))
a.extend(['code'])
print(a)
print(len(a))
a.extend('moon')
#print(a)
#print(len(a))
a.remove('o')
#print(a)

#clear()-->removes all elements and returns
#empty list
a=[12,5,8,'am',123]
#a.clear()
#print(a)
#a.extend([1,5,8,9])
#print(a)

del a[1:4]
print(a)

a=[1,5,-56,12,3,4,6]
print(a)
#sort()-->arrange elements in ascending
#alphabetical order
a.sort()
print(a)
#reverse()-->gives elements in reverse order
a.reverse()
print(a)

#min(),max(),len()
a=[1,5,-56,12,3,4,6]
print(min(a))
print(max(a))

a=[1,2,3,5]
b=a+a #merging lists
print(b)

c=[1,3*'p']
d=c*2 #repetition
print(d)


#Tuples-->It is an immutable collection
#which can have same/different objects enclosed
#within parenthesis()

a=()
print(a)
print(type(a))

a=(1,2,3,4,5)
print(a)
print(len(a))
#a[2]=45 #tuples are immutable

b=(1,2,[1,2,45],'code')
#we can use list methods above
#b[-2].extend([450,23])
#print(b)
#we can perform any operations on list inside tuple
#b[-2].sort()#assending order
#print(b)

#print(min(b))
print(min(b[-2]))#check carefully all objects in tuple
print(max(b[-2]))

#a=[1,8,9]
#a.extend(('p',456))
#print(len(a))

#Every builtin datatype is a built-in function
a="codegnan"
b=list(a)
print(b)
b.sort()
print(b)

#[]-->Lists,()-->Tuples
#{}-->Sets and Dictionaries

#Sets are Unorder Collection with only
#unique elements each object separated by comma in{}

a={5,1,-23,1,2,4,5}
print(a)
print(type(a))

#Sets are Mutable-->,update(),remove()..
a={5,1,-23,1,2,4,5}
#a.add(25)#adds elements to set any where
#print(a)
#a.add('poll')
#print(a)
#update()
a.update([78,56,12])
print(a)
a[2]=45#no indexing,slicing
print(a)

#remove()discard(),pop(),clear()
a={45,31,55,21,'jeeva'}
a.remove(45)
print(a)
#a.remove(22)#raises KeyError as no element
print(a.discard(22))
print(a)

a={45,31,55,21,'jeeva'}
a.pop()#removes orbitary elements from set
print(a)
a.clear()
print(a)#empty set-->set()

#union(),intersection(),difference()....

a={4,6,7,8,40,1}
b={'c',34,67,12,40}
print(a.union(b))#combination of multiple sets 
print(a.intersection(b))#picks common elements
print(a.difference(b))
print(b.difference(a))
#picks common elements and prints
#elements fromfirst set
print(a.difference(b))
print(b-a)'''
#symmetric_difference-->^
#removes common elements and gives all other
#elements
a={4,6,7,8,40,1}
b={'c',34,67,12,40}
print(a.symmetric_difference(b))
print(b^a)
print(a)
a.intersection_update(b)
print(a)

'''#Dictionaries
#An Orderd collections of key-value pairs
#where key must be unique

a={1:1,2:4,3:9}
#print(a)
#print(type(a))
#print(len(a))
#we access only by giving key
#print(a[1])#returns key error if we give wrong key
#print(a[2])
#print(a[3])

data={'idnos':[45,24,15],
      'names':['code','python'],
      'age':[21,31]}
print(data)      

#keys(),values()
print(data.keys())#returns keys from dictionary
print(data.values())
print(data['names'])
print(type(data['names']))
data['names'].extend(['jeeva','python'])      
print(data['names'])
      
#sort idnos from above data
data['idnos'].sort()
#print(data['idnos'])

#Dictionaries are Mutable
data['places']=['Tnk','Gnt']
print(data)
#update()->needs only dictionary format
data.update({14:45,12:144})
print(data)'''


'''b={'name':'codegnan',
   'place':'amreddy',
   'course':'python'}
print(b)
#remove from dictionary
b.pop('place')
print(b)
b.pop('name')
print(b)
print(b.popitem())#removes last pair
print(b)'''

#items(),fromkeys()
'''print(b.items())#reurns key-value pairs

#fromkeys()
a=['name',25,36]
#c=dict(a)#raises Error as we need to have pair 
#print(a)

#takes every object as key and value will be None
c=dict.fromkeys(a)
print(c)
c['name']='jeeva'
print(c)'''


































      





      
