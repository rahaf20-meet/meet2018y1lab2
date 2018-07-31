Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> a = 5
>>> b = 10
>>> a = b
>>> b = a
>>> b
10
>>> a
10
>>> a = 5
>>> b = 10
>>> b = a
>>> a
5
>>> b
5
>>> a = 5
>>> b = 10
>>> c = 5
>>> a = b
>>> b = c
>>> a
10
>>> b
5
>>> four = '4'
>>> print(four*3)
444
>>> five = 4
>>> print(five)
4
>>> print(five*3)
12
>>> my_name = 'student'
>>> print (my name is ' + 'my _name
	   
SyntaxError: invalid syntax
>>> print("my name is " + my_name)
	   
my name is student
>>> my name is student
	   
SyntaxError: invalid syntax
>>> print("my name is ' +
	  
SyntaxError: EOL while scanning string literal
>>> print("hi," + my_name)
	  
hi,student
>>> my_age = 15
	  
>>> print("I am" + my_age + "years old")
	  
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print("I am" + my_age + "years old")
TypeError: must be str, not int
>>> print("I am + my_age + years old")
	  
I am + my_age + years old
>>> str(15)
	  
'15'
>>> print("I am + my_age + years old")
	  
I am + my_age + years old
>>> print("I am" + "15" + "years old")
	  
I am15years old
>>> print("I am " + str(my_age) + " years old")
	  
I am 15 years old
>>> score = 1
	  
>>> total = score + (count * 2)
	  
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    total = score + (count * 2)
NameError: name 'count' is not defined
>>> count = 5
	  
>>> total = score + (count * 2)
	  
>>> print(total)
	  
11
>>> endlab
	  
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    endlab
NameError: name 'endlab' is not defined
>>> type(2.1+6)
	  
<class 'float'>
>>> a="cat"
	  
>>> b=5
	  
>>> a=b
	  
>>> print(b)
	  
5
>>> hello = "hi"
	  
>>> bye = " goodbye"
	  
>>> print(hellobye)
	  
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(hellobye)
NameError: name 'hellobye' is not defined
>>> 28*4
	  
112
>>> 5613+112
	  
5725
>>> print("guess a number")
	  
guess a number
>>> guess = guess a number
	  
SyntaxError: invalid syntax
>>> guess
	  
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    guess
NameError: name 'guess' is not defined
>>> guess = "guess a number"
	  
>>> print(guess)
	  
guess a number
>>> name = rahaf
	  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    name = rahaf
NameError: name 'rahaf' is not defined
>>> name = "rahaf"
	  
>>> name
	  
'rahaf'
>>> n=4
	  
>>> while n>0:
	  print(n)
	  n=n-1

	  
4
3
2
1
>>> n= int(input("guess a number"))
	  
guess a number3
>>> x = 5
	  
>>> while n<x:
	  print(too low!)
	  
SyntaxError: invalid syntax
>>> while n<x:
	  print("too low")
	  
