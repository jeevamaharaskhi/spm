#Built-in Modules -->math,time,datetime,
#os,random,calendar...
#datetime module -->date,time,datetime and
#timedelta..
'''
import datetime
#help(datetime)
#get current date and time
a = datetime.datetime.now()
#print(a)
#print(type(a))
#only date from above object
d = a.date()
print(d)
f = a.time()
print(f)

#we can use from keyword to use specific
#methods/functions from a module

from datetime import date,time
a = date(2023,3,22)#year,month,day
print(a) 
b = date(day=20,month=5,year=2025)
print(b)

d,m,y = map(int,input("enter the numbers:").split(','))
print(d,m,y)
#new = date(y,m,d)
#print(new)
f = time(10,17)
print(f)
'''
#strftime()-->string format of time
#%d ->day of the month,%b-->short name of month
#%y -->two digit year,%B-->full name of month
#%Y-->four digit year format
from datetime import date,time,datetime
a = date.today() #or datetime.now()
#print(a)

d=a.strftime("%d-%b-%y")
print(d)
f = a.strftime("%D,%B,%Y")
print(f)
h = a.strftime("Today is %A")
h = a.strftime("Today is %a")
#%A -->full name of day of week
#print(h)
#print(h.upper())
k = a.strftime("Today is %j day of year")
#print(k)
'''
#picking date as inputs from user -->date format
n = date(2023,4,14)
#print(n.strftime("It is %B and %A,%j of year"))

#calendar module-->print mnth,year calendar
import calendar
#m = int(input("Enter a month (1-12)"))
#y = int(input("Enter the year"))
#print month calendar
#n = calendar.month(y,m)
#print(n)
#complete calendar of a year
#h = calendar.calendar(y)
#print(h)

#random module -->It is used to generate
#psuedo random number/pick choice of inputs
#Number Guessing..
import random
import time
#print(dir(random)) #help(random)
#randint(a,b) generates values within a &b
#print(random.randint(1,10))
#we want to generate a group -->OTP
for i in range(5):
    print(random.randint(1000,9999))
    time.sleep(10) #halting duration

#print(random.randrange(5,40,5)) #divisble

#Number Guessing game
number = random.randint(1,10)
guess = int(input("Enter the number(1-10)"))
while guess!=number:
    if guess < number:
        print("oops you hve entered lower number")
        guess = int(input("Enter again"))
    elif guess > number:
        print("ohho higer number")
        guess = int(input("Enter again"))
print("Bingo got it...")

#choice(seq) -->takes any random object from
#the sequence #-->Rock,Paper,Scissors game
#Story Generation game
for i in range(5):
    player1 = input("Enter any-->Rock,\
    Paper,Scissor").lower()
    #print(player1)
    player2 = random.choice(['rock','paper','scissor'])
    if player1 == "rock" and player2 == "paper":
        print("Player2 won")
    elif player1 = "paper" and player2 == "scissor":


#QRcode / Email Automation

#QRcode -->pyqrcode,pypng
#pip install pypng
#pip install pyqrcode

import pyqrcode
import png
#take a link to create QRcode
link = "https://www.codegnan.com/"
qr=pyqrcode.create(link)
#create an image for above qrcode
#print(qr)
qr.png("website.png",scale=8)

#segno -->create your own business card
import segno
#help(segno)
#print(dir(segno))
from segno import helpers
card = helpers.make_mecard(name="Saketh Kallepu",
                           email ="saketh@codegnan.com",
                           phone="+91 8106429771",
                           url="https://www.linkedin.com/saketh-codegnan",
                           birthday="1993/12/26")
#save in png format
card.save("mycard.png",scale=10)'''
