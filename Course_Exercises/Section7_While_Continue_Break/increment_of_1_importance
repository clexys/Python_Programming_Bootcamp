''' You need to increment i before continue because continue jumps 
back to the start of the loop again. If you don't increment i will 
keep the same value and you'll have an infinite loop. This code should explain. 
Try changing it by getting rid of the increment and see what happens. '''

import random

i = 1
while i < 20:
    print(f"Start of While | i = {i}")
    if i % 2 == 0:
        i += 1
        print(f"Hit Continue | i = {i}")
 
    if i == 15:
        print(f"Hit Break | i = {i}")
        break
 
    i += 1
    print(f"Found Odd | i = {i}")
 
print(f"Out of While | i = {i}")
