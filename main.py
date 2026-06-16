import random

numbers_list = random.sample(range(0, 10), 5)
print(numbers_list)

code_list = ['*', '*', '*', '*', '*']
print(code_list)

print("Enter a numbers: ")
match_count_places = 0
match_count = 0
for i in numbers_list:
    your_number = int(input())
    if your_number == i:
        match_count_places += 1
    if your_number in numbers_list:
        match_count += 1

print(f"Match numbers: {match_count}")
print(f"Match numbers in their places: {match_count_places}")

#TODO: pygame