"""Password generater"""
import string
import random
print("Wlecome To Password Generator")
while True:
    try:
        l=int(input("Enter The length of the password : "))
        if(l<=0):
            print("The length should be atleast greater then 0. Try again .")
            continue
        break
    except ValueError:
        print("The length should be a number only. Try again ")
while True:
    ans=input("Do you want letter in your password y/n : ").lower()
    if(ans=='y'):
        a=True
        break
    elif (ans=='n'):
        a=False
        break
    else: 
        print("Please type y or n only")
while True:
    ans=input("Do you want numbers in your password y/n : ").lower()
    if(ans=='y'):
        b=True
        break
    elif (ans=='n'):
        b=False
        break
    else: 
        print("Please type y or n only")
while True:
    ans=input("Do you want special characters in your password y/n : ").lower()
    if(ans=='y'):
        c=True
        break
    elif (ans=='n'):
        c=False
        break
    else: 
        print("Please type y or n only")
n=""
if a:
    n+=string.ascii_letters
if b:
    n+=string.digits
if c:
    n+=string.punctuation
if not n:
    print("characters cant be empty")
    exit()
password=''.join(random.choices(n,k=l))
print("The generated password is : ",password)

