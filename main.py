import random

numbers_list = [random.randint(0, 9) for _ in range(5)]
print(numbers_list)
code_list = ['*', '*', '*', '*', '*']
print(code_list)

your_number = int(input("Enter a number: "))

for i in numbers_list:
    if your_number == i:
        print("Match")
    else:
        print("No match")