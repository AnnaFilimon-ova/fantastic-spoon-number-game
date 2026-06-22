import random
import pygame
import sys
#cd fantastic-spoon-number-game
#source myenv/bin/activate
pygame.init()

screen = pygame.display.set_mode((400,200))
pygame.display.set_caption("Password cracking")
clock = pygame.time.Clock()

font1 = pygame.font.Font(None, 100)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None, 30)

user_text = ""
input_active = True

match_count = 0
match_count_places = 0

numbers_list = random.sample(range(0, 10), 5)

text_image2 = font2.render("_______________", True, (0, 255, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                if len(user_text) == 5:
                    user_numbers = [int(d) for d in user_text]
                    match_count_places = 0

                    for i in range(5):
                        if user_numbers[i] == numbers_list[i]:
                            match_count_places += 1
                    match_count = len(set(user_numbers) & set(numbers_list))

                    if match_count_places == 5:
                        print("YOU WIN!")
                        input_active = False

            else:
                if event.unicode.isdigit() and len(user_text) < 5:
                    user_text += event.unicode

    display_text = user_text 
    text_image1 = font1.render(display_text, True, (0, 255, 0))

    match_count_str = f"Match numbers: {match_count}"
    match_count_places_str = f"Match numbers in their places: {match_count_places}" 

    text_image3 = font3.render(match_count_str, True, (0, 255, 0))
    text_image4 = font3.render(match_count_places_str, True, (0, 255, 0))

    screen.fill((0, 0, 0))
    screen.blit(text_image1, (90, 18))
    screen.blit(text_image2, (0, 40))
    screen.blit(text_image3, (10, 125))
    screen.blit(text_image4, (10, 155))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()