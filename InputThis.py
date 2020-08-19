"""
welcome = "Hello"
print("Enter name: ")
name = input()
print(welcome + ' ' + name)
"""

"""
#different ways of accepting inputs
print("enter first number: ")
number1 = int(input())
number2 = int(input("Please enter second number: "))
print(number1 + number2)
"""
"""
#string formatting
name = "Phil"
age = 50
#not a good wway to fomat:
print ("my name is "+name + ' and I am ' + str(age) + " years old")
#preferred way to formatting
#use {} - acts as a placeholder for the variable
print("My name is " + name + " and I am {0}".format(age) + " years old")
print("My name is {0} and I am {1} years old".format(name,age))
"""

"""
#For loops
for i in range(0,200):
    print("i is now {0}".format(i))
"""

"""
#arrays
#initialize an arrray
arr =  [1,2,3,4,5,6]
print(arr[1])
print(arr[-1]) #-1 gets the end of the array
print('----')
arr2 = [1,"test"]
print(arr2[0])
print(arr2[-1])
"""

#if
import random #this is a library

number = random.randint(1,10)
tries = 1

print("Choose a number between 1 and 10")
guess = int(input("Guess what it is: "))
if guess > number:
    print("too high")
if guess < number:
    print("too low")
