"""Bug-Fixing Exercise 1
The code below has two bugs. Hunt them down and fix them.

while True
print("Hello")"""

#Solutions

while True:
    print("Hello")

"""Bug-Fixing Exercise 2
The programmer here is trying to convert the string "hello" to "HELLO" by using the upper() method:

greeting = "hello"
print(upper(greeting))
However, the program returns an error. Can you help fix the code, so it prints out HELLO?"""

#Solutions

greeting = "hello"
print(greeting.upper())

"""A programmer wrote the following program:

countries = []
 
while True:
    country = input("Enter the country: ")
    countries.append(country)
print(countries)
The expected output is as follows:"""

#Solutions

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)
