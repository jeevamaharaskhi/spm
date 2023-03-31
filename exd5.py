'''
A module is python file consisting of functions,
datatypes,classes...where we use
import Day5
#print(dir(Day5))
#Day5.check()
#print(Day5.data)
#print(Day5.data.keys())
#python provides a bunch of modules in-built
#such as time,random,os,math...

#math module-->it contains all mathematical
#constants,function,trignometric...
import math
#help(math)
print(math.pi)
print(math.factorial(5))
print(math.log(1))
print(math.log10(1))
print(math.sqrt(25))
a=25**0.5
print(a)
'''
#time module-->fetch current time,timer
#logic..
import time
#help(time)
d=time.time()#it returns epoch time
#from 1970 jan1st
#print(d)
#we can check execution time of a program
'''for i in range(10):
    print(i**2)
e=time.time()
print(e-d)'''

'''for i in range(10):
    print(i**2)
    time.sleep(5)#sleep(seconds)halts
e=time.time()
print(e-d)'''

#to get current date and time
#ctime
d=time.ctime()
print(d)
print(len(d))


e=time.localtime()
print(e)
#pick only date
d=e.tm_mday
m=e.tm_mon
y=e.tm_year
print(f'{d}/{m}/{y}')
h=e.tm_hour
m=e.tm_min
print(f'{h}:{m}')





















