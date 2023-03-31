#Email Automation using Python
#smtplib -->Simple Mail Transfer Proctol
'''import smtplib
#connect to the server(initialization)
server = smtplib.SMTP('smtp.gmail.com',
                      587)
#start the server
server.starttls()
#login
server.login('saketh@codegnan.com',
             '') #mention your pswd
#give your message
msg = "Hello first mail using Python"
#send mail
server.sendmail("saketh@codegnan.com",
                "saikumarduba143@gmail.com",msg)

#To add subject and to address while sending
#email -->email package along with smtp
#import email
import smtplib
#MIME -->Multipupose Internet Mail Extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#start defining the fields
sender = "saketh@codegnan.com"
receiver = "mohankumargalla@gmail.com"
subject = "Today we are in CRT class"
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
body = "Hello guys hope you are following"
#attach the body of the message
msg.attach(MIMEText(body,'plain'))
txt = msg.as_string()
#add first simple mail code
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,'ecgitozompnxiylv') #give you app passcode
server.sendmail(sender,receiver,txt)
print("Mail sent success")

#Now we are adding attachment
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#for adding attachment
from email.mime.base import MIMEBase
from email import encoders
import os #to read files from local system
#start defining the fields
sender = "saketh@codegnan.com"
pwd = "ecgitozompnxiylv" #give you app passcode
receiver = "mohankumargalla@gmail.com"
subject = "Today we are in CRT class"
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
body = "Hello guys hope you are following"
#we will give our attachment
attach = "day6.py" #give your attachment here
msg.attach(MIMEText(body))
#read the attachment
part = MIMEBase('application',
                'octet-stream')
part.set_payload(open(attach, 'rb').read())
#encode the attachment data
encoders.encode_base64(part)
#adding header to the attachment
part.add_header('Content-Disposition',
   'attachment; filename="%s" '
                % os.path.basename(attach))
msg.attach(part)
txt = msg.as_string()
#add first simple mail code
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,pwd) #give you app passcode
server.sendmail(sender,receiver,txt)
print("Mail sent success")
'''
#os module -->It interacts with our operating
#system

import os
#let's get the current working drctry
print(os.getcwd())
#we can get the list of all directories/files
#listdir()
#print(os.listdir())

#Write a program to get only txt and py files
#from the current loctn
d = os.listdir()
'''e = []
for i in d:
    if i.endswith('.py') or i.endswith('.txt'):
        #print(i,end=' ')
        e.append(i)
print(e)
print(len(e))
'''
#create,remove,rename files/folders
#mkdir() -->make drctry
#remove() -->removes a file (permanent)
#removedirs() -->removes a folder
#print(os.getcwd())

#print(os.mkdir('saketh')) #give your desrd name
#print(os.listdir())

#to check whether a folder/file is existing/not
#print(os.path.isdir('saketh'))
#print(os.path.isfile('day1.py')) #for file checking

#remove a file/folder (permanent)
#print(os.removedirs('saketh'))

#os.remove('C:/Users/codeg/Desktop/AM Sessions/edited.png')
#rename a file/folder -->rename()
#print(os.listdir())
#os.rename('website.png','web.png')
#print(os.listdir())
#getcwd(),listdir()

#Comprehensions -->One liner expressions
#List Comprehensions
#Syntax for List Comprehensions

#[exprsn for var in iterable/range [optional if/else for]]
'''
a = ['codegnan','saketh','python']
b = []
for i in a:
    b.append(i.upper())
print(b)

c= [i.upper() for i in a]
print(c)

a = [1,5,8,9,12]
#b = [1,25,64,81,144]

b=[i**2 for i in a]
print(b)

c = [i**2 for i in range(1,11)]
print(c)
'''
#we can add if block for above comprehension
d = [i**2 for i in range(1,11) if i%2==0]
#print(d)
#print(sum(d))

#we can add multiple conditions...

e = [i for i in range(1,50) if i%3==0 if i%5==0]
#print(e)

#if-else block with List comprehensions
e = [i**2 if i%2==0 else "Odd"
     for i in range(1,51)]
#print(e)

#No elif in List comprehension we can add multiple
#if,else blocks....

a = ["Saketh" if i%3==0 and i%5==0 else
     "Codegnan" if i%3==0 else "Python"
     if i%5==0 else i for i in range(51)]
print(a)






























