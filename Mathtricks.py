#!/usr/bin/env python3
part1=''
part2=''
part3=''
part4=''

print(f"You are about to witness an unbelievable trick.(Please do try at home, if you can) \n\n")

number = 0
print("Step 1: Pick any number between 1 and 10.(Remember your choice)\n")
input()

part1=str(input("Step 2: Multiply your number by 3, and divide by 2.\nIf your answer is a whole number(not a decimal), type 'yes', and if is a decimal, type 'no'.\n"))

if ((part1 == "yes") or (part1 == "Yes")):
    part2=str(input("Step 3: Please repeat step 2 on your new number, and  type 'yes'if it is a whole number, and if is a decimal, type 'no'.\n"))

elif ((part1 =="no") or (part1 == "No")):
    number += 1
    print("\nRound off your number to the next number.")
    input()
    part2=str(input("Step 3: Please repeat step 2 on your new number, and  type 'yes'if it is a whole number, and if is a decimal, type 'no'.\n"))
    
if ((part2 == "Yes") or (part2 == "yes")):
    part3=str(input("Step 4: Add 2 to your new number, and subtract 11. Type 'yes' if your number is negative, and 'no' if your number is positive or zero.\n"))
elif ((part2 =="no") or (part2 == "No")):
    number += 2
    print("\nRound off your number to the next number.")
    input()
    part3=str(input("\nStep 4: Add 2 to your new number, and subtract 11. Type 'yes' if your number is negative, and 'no' if your number is positive or zero. \n"))
                    
if ((part3 == "Yes") or (part3=="yes")):
    print("\nYour number is", number)
elif ((part3 == "No") or (part3== "no")):
    number += 4
    part4=str(input("\nStep 5: Please repeat step 4. Type 'yes' if your number is negative, and 'no' if your number is positive or zero.\n"))

if ((part4 == "Yes") or (part4=="yes")):
    print("\nYour number is", number)
elif ((part4 == "No") or (part4=="no")):
    number += 4
    print("\nYour number is", number)
