#!/usr/bin/env python
# coding: utf-8
1. Calculate Area of a Circle
Write a Python program which accepts the radius of a circle from the user and compute the area. 
# In[1]:


radius = float(input("Enter Radius: "))
import math
Area = math.pi * radius**2
print(f"Area of circle with given radius is {Area}" ".")

2. Check Number either positive, negative or zero
Write a Python program to check if a number is positive, negative or zero 
# In[15]:


inp=int(input("Integer Checker: "))
if inp>0:
    print("The Given Number is Positive .")
elif inp<0:
    print("The Given Number is  Negative .")
elif inp==0:
    print("The Given Number is Zero .")
else:
    print("The Given Number is  Not an integer .")

3. Divisibility Check of two numbers
Write a Python program to check whether a number is completely divisible by another number. Accept two integer
values form the user 
# In[3]:


dividend=int(input("Enter numerator :"))
divisor=int(input("Enter denominator :"))
if dividend%divisor==0:
    print(f"Number {dividend} is Completely divisible by {divisor}")
else:
    print(f"Number {dividend} is not Completely divisible by {divisor}")

4. Days Calculator
Write a Python program to calculate number of days between two dates 
# In[ ]:


from datetime import datetime
date_format = "%d/%m/%Y"
e = input("Enter a date in (dd/mm/yy) Format: ")
f = input("Enter a date in (dd/mm/yy) Format: ")
a = datetime.strptime( e , date_format)
b = datetime.strptime( f , date_format)
delta = b - a
print ("There are", delta.days, "days in Between", e , "and" , f)

5. Calculate Volume of a sphere
Write a Python program to get the volume of a sphere, please take the radius as input from user 
# In[4]:


radius = float(input("Enter Radius: "))
import math
volume = (4/3) * math.pi * radius**2
print(f"Volume of circle with radius is {volume}")

6. Copy string n times
Write a Python program to get a string which is n (non-negative integer) copies of a given string. 
# In[5]:


st=input("Enter String: ")
n=int(input("How many copies of String you need:"))
for i in range (0,n):
    print(st,end="")

7. Check if number is Even or Odd
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate
message to the user 
# In[6]:


num=int(input("Enter no.: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

8. Vowel Tester
Write a Python program to test whether a passed letter is a vowel or not
# In[7]:


ch=input("Enter a character: ").upper()
if ch=="a":
    print(f"Letter {ch} is Vowel")
elif ch=="e":
    print(f"Letter {ch} is Vowel")
elif ch=="i":
    print(f"Letter {ch} is Vowel")
elif ch=="o":
    print(f"Letter {ch} is Vowel")
elif ch=="u":
    print(f"Letter {ch} is Vowel")
else:
    print(f"Letter {ch} is not Vowel")

9. Triangle area
Write a Python program that will accept the base and height of a triangle and compute the area 
# In[8]:


base=float(input("Enter base of triangle: "))
height=float(input("Enter height of triangle: "))
print(f"Area of triangle is: {(base * height)/2}")

10. Calculate Interest
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number
of years 
# In[9]:


principle = float(input("Please enter principal amount: "))
interest = float(input("Please Enter Rate of interest in %: "))
years = float(input("Enter number of years for investment: "))
value = principle*(1+interest)**years
print(f"After {years} years your principal amount {principle} over an interest rate of {interest} % will be {value}")

11. Euclidean distance
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# In[10]:


x1=int(input("Enter Co-ordinate for x1: "))
x2=int(input("Enter Co-ordinate for x2: "))
y1=int(input("Enter Co-ordinate for y1: "))
y2=int(input("Enter Co-ordinate for y2: "))
dist=int(((x1-y1)**2 + (x2-y2)**2)**(1/2))
print(f"Distance between points ({x1}, {x2}) and ({y1}, {y2}) is {dist}")

12. Feet to Centimeter Converter
Write a Python program to convert height in feet to centimetres. 
# In[11]:


height=float(input("Enter Height in Feet: "))
print(f"There are {30.48*height} Cm in {height} ft")

13. BMI Calculator
Write a Python program to calculate body mass index 
# In[12]:


height=float(input("Enter Height in cm: "))
weight=float(input("Enter Weight in Kg: "))
bmi=(weight/(height**2))*(100**2)
print(f"Your BMI is {bmi}")

14. Sum of n Positive Integers
Write a python program to sum of the first n positive integers 
# In[13]:


a = int(input("Enter value of n: "))
i = 1
total = 0
while i <= a:
    total += a
    i += 1 
    
print(total

15. Digits Sum of a Number
Write a Python program to calculate the sum of the digits in an integer 
# In[1]:



a = str(input("Enter a Number: "))
b = 0 
for x in a:
    b += int(x)
print("Sum of", '+'.join(map(str,a)) ,"is: ",b)

16. Decimal to Binary Converter
Write a Python program to convert an decimal integer to binary
# In[3]:


decimal = int(input("Enter a Decimal number: "))
e = bin(decimal)
print("The Binary Reperesentation of",decimal,"is: ", e[2:])

18. Vowel and Consonants Counter
Input a text and count the occurrences of vowels and consonant 
# In[ ]:


a = input("Enter Text: ")
c = a.lower()
d = 0
f = 0
for x in c:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        d += 1
    else:
        f += 1
print("Vowels: ",d)
print("Consonants: ",f)

19. Palindrome tester
Write a program to check whether given input is palindrome or not 
# In[ ]:


a = input("Enter Text: ")
if a == a[::-1]:
    print("Text",a,"is Palindrome. ")
else:
    print("Text ",a,"is Not Palindrome. ")

23. Write a Python program to construct the following pattern 
# In[5]:



a= 1
b = 0
while b <= 9:
    c = '*'
    print(c * a)
    a =a+ 1
    b =b+1

21. Write a Python program to construct the following pattern 
# In[6]:



f1 = 1
i1 = 0
f2 = 4
i2 = 0
while i1 <= 4:
    d = '*'
    print(d * f1)
    f1 += 1
    i1 += 1
while i2 < 4:
    d = '*'
    print(d * f2)
    f2 -= 1
    i2 += 1

22. Write a Python program to construct the following pattern 
# In[13]:


i=9
d = 0
for x in range(1,i):
    for y in range(1, x + 1):
        print (y , end = " ")
    print(" ")
for r in range(i,d,-1):
    for c in range(1, r + 1):
        print (c , end = " ")
    print(" ")


# In[ ]:




