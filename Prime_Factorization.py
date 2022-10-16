import math
import sys


def find_factors(num):
    list_end = int(num / 2)
    num_list = []
    factors = []
    for x in range((list_end + 1)):
        num_list.append(x)
    num_list.pop(0)
    for x in num_list:
        number = num / x
        y = str(number)
        y = int(y[-1])
        if y == 0:
            factors.append(x)
    return factors


def isprime(num):
    prime_flag = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        return True
    else:
        return False


if len(sys.argv) > 1:
    try:
        num_to_be_factorized = int(sys.argv[1])
    except Exception as e:
        num_to_be_factorized = int(input("Enter the number you want prime factorized: " + "\033[31m" + "\033[1m"))
else:
    num_to_be_factorized = int(input("Enter the number you want prime factorized: " + "\033[31m" + "\033[1m"))
print("\033[0m", end="")
if isprime(num_to_be_factorized):
    print("The number you entered is prime.")
    exit()

num_list = []
factors = []
nums_to_be_printed = []

for q in range(1, num_to_be_factorized):
    if isprime(q):
        num_list.append(q)

num = num_to_be_factorized

while True:
    divisors = []
    for x in num_list:
        if num % x == 0:
            divisors.append(x)
    try:
        factors.append(divisors[1])
        nums_to_be_printed.append(num)
    except IndexError as e:
        """print(" |1")"""
    try:
        num = int(num / divisors[1])
    except IndexError:
        break
    if find_factors(num) == [1, num]:
        break
del x
longest = len(str(factors[-1]))
divisors_list_to_be_printed = factors[::1]
nums_list_to_be_printed = nums_to_be_printed[::1]
x = 0
i = 0

for x in divisors_list_to_be_printed:
    number_of_spaces = longest - len(str(x))
    print(" " * number_of_spaces, end="")
    print("\033[1m" + "\033[37m" + "\033[4m" + str(x), end="")
    print("|", end="")
    print(str(nums_list_to_be_printed[i]) + "\033[0;0m")
    i += 1
else:
    print(" " * longest, end="")
    print("\033[1m" + "\033[37m" + "\033[4m" + "|1" + "\033[0;0m")
    
print()

x = 0
print("\033[33m" + "\033[1m")
for x in factors:
    print(x, end=" ")
print("\033[0;0m")
