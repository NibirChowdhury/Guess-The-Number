"""
1. Tell him to multiply the chosen number by 2.
2. Choose an even number to use yourself. Ask your friend to add this number to the one in their head.
3. Tell them to divide the new number by 2.
4. Tell them to subtract their original number from the equation.
    "Guess" the number."""
import msvcrt as m
import random
def wait():
    m.getch()

print("Remind a number and press enter")
wait() 
print("Multiply it with 2 and press enter")
wait() 
number = ((random.randint(0,99)*2))
print("I give you ", number," to add and press enter")
wait()
print("Now divide it into half and press enter")
wait()
print("Subtract your number from the whole sum-up and press enter")
wait()
result = number/2
print("You have ", result, " remain")


