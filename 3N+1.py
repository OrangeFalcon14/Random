import matplotlib.pyplot as plt

# Best numbers are : 11111, 111, 111111, 33, 333

number = int(input("Enter a number:"))
old_val = None
numbers = [number]
while(True):
    if old_val == 1:
        break
    if number % 2 == 0:
        number /= 2
    else:
        number = (number * 3) + 1
    print(int(number))
    old_val = number
    numbers.append(int(number))
    
x_points = [x[0] for x in enumerate(numbers, start=0)]

plt.plot(x_points, numbers)
plt.show()
