import random

numbers_list = random.sample(range(0, 10), 5)

print("* * * * *")

print("Enter a numbers: ")
match_count_places = 0
match_count = 0

while match_count_places != 5:

    user_numbers = input()
    your_numbers = [int(num) for num in user_numbers.split()]
    match_count_places = 0
    match_count = 0
    for i in range(5):
        if your_numbers[i] == numbers_list[i]:
            match_count_places += 1
    match_count = len(set(your_numbers) & set(numbers_list))
    print(f"Match numbers: {match_count}")
    print(f"Match numbers in their places: {match_count_places}")
    
print("You win!")

#TODO: pygame