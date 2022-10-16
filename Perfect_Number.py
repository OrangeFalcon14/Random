#!/usr/bin/env python3
import math

def find_factors(num):
    list_end = int(num/2)
    num_list = []
    factors = []
    for x in range((list_end + 1)):
        num_list.append(x)
    num_list.pop(0)
    for x in num_list:
        number = num/x
        y = str(number)
        y = int(y[-1])
        if y == 0:
            factors.append(x)
    return factors

number = 1

verbose = 1 if input("Print every number? If no, only perfect numbers will be printed (y/n): ") == "y" else 0

print("\n")

while True:
    if verbose:
    	print(f"Trying:{number}")
    
    factors = find_factors(number)
    sum_of_list = 0
    for x in factors:
        sum_of_list += x
    if sum_of_list == number:
        print(f"{number} is a perfect number!")
    number += 1
