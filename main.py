import random
import pygame
import sys
#cd fantastic-spoon-number-game
#source myenv/bin/activate

#* Prints
symbols = "* * * * *"
match_count = 0
match_count_places = 0
match_count_str = f"Match numbers: {match_count}"
match_count_places_str = f"Match numbers in their places: {match_count_places}" 

font1 = pygame.font.Font(None, 120)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None, 30)

text_image1 = font1.render(symbols, True, (0, 255, 0))
text_image2 = font2.render("_______________", True, (0, 255, 0))
text_image3 = font3.render(match_count_str, True, (0, 255, 0))
text_image4 = font3.render(match_count_places_str, True, (0, 255, 0))

#! Game
pygame.init()

screen = pygame.display.set_mode((400,200))
pygame.display.set_caption("Password cracking")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text_image1, (70, 30))
    screen.blit(text_image2, (0, 40))
    screen.blit(text_image3, (0, 125))
    screen.blit(text_image4, (0, 155))
    
    numbers_list = random.sample(range(0, 10), 5)

    #TODO: enter a numbers

    '''
    while match_count_places != 5:
        user_numbers = input()
        your_numbers = [int(num) for num in user_numbers.split()]
        match_count_places = 0
        match_count = 0
        for i in range(5):
            if your_numbers[i] == numbers_list[i]:
                match_count_places += 1
        match_count = len(set(your_numbers) & set(numbers_list))
        match_count_str = f"Match numbers: {match_count}"
        match_count_places_str = f"Match numbers in their places: {match_count_places}"
        
        
    print("You win!")
    '''


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()