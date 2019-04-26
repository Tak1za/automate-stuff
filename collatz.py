import random

def collatz(number):
    if(number % 2 == 0):
        print (number // 2)
        return (number // 2)
    else:
        print (number * 3 + 1)
        return (number * 3 + 1)

while(True):
    print ('Enter number:')
    try:
        num = int(input())
        if(collatz(num) == 1):
            break
    except ValueError:
        print ('Please enter an integer')