"""
Program Description: A Fruit Catch type game created for LMUHacks 2023 and visually themed to promote food drives
Author: Milo Fritzen
Date: 4/15/2023
References:
Collaborators: Chris Beaudoin

NOTE:
I used the word cans for my variable names but we changed
directions with the sprites after writing the code so ignore that
"""

# imports
import pygame
import random
import sys


# functions
def move_basket():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_rect.left > 0:
        basket_rect.left -= B_SPEED
    elif keys[pygame.K_RIGHT] and basket_rect.right < WIDTH:
        basket_rect.left += B_SPEED


def drop_cans():
    global score
    for i in range(len(can_rects)):
        can_rects[i].top += can_speeds[i]

        # Check for collision with basket
        if can_rects[i].top > HEIGHT:
            # Can missed
            can_image = random.choice(can_images)
            can_rects[i] = can_image.get_rect()
            can_rects[i].left = random.randint(0, WIDTH - can_rects[i].width)
            can_rects[i].top = random.randint(-HEIGHT, -can_rects[i].height)
            can_speeds[i] = random.randint(3, 8)
            score -= 1

        if can_rects[i].colliderect(basket_rect):
            # Can caught
            can_image = random.choice(can_images)
            can_rects[i] = can_image.get_rect()
            can_rects[i].left = random.randint(0, WIDTH - can_rects[i].width)
            can_rects[i].top = random.randint(-HEIGHT, -can_rects[i].height)
            can_speeds[i] = random.randint(3, 8)
            score += 1


def drop_evil_cans():
    global score
    for i in range(len(evil_can_rects)):
        evil_can_rects[i].top += evil_can_speeds[i]

        # Check for collision with basket
        if evil_can_rects[i].top > HEIGHT:
            # Evil can missed
            evil_can_image = random.choice(evil_can_images)
            evil_can_rects[i] = evil_can_image.get_rect()
            evil_can_rects[i].left = random.randint(0, WIDTH - evil_can_rects[i].width)
            evil_can_rects[i].top = random.randint(-HEIGHT, -evil_can_rects[i].height)
            evil_can_speeds[i] = random.randint(3, 8)
            score += 1

        if evil_can_rects[i].colliderect(basket_rect):
            # Evil can caught
            evil_can_image = random.choice(evil_can_images)
            evil_can_rects[i] = evil_can_image.get_rect()
            evil_can_rects[i].left = random.randint(0, WIDTH - evil_can_rects[i].width)
            evil_can_rects[i].top = random.randint(-HEIGHT, -evil_can_rects[i].height)
            evil_can_speeds[i] = random.randint(3, 8)
            score -= 5


def update_sprite():
    return random.choice(can_images)


def update_screen():
    # Update the screen
    bg_img = pygame.image.load('background.jpg')
    bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
    window.blit(bg_img, (0, 0))

    window.blit(collection_basket, basket_rect)
    for i in range(len(can_rects)):
        window.blit(can_images[i % 2], can_rects[i])
    for i in range(len(evil_can_rects)):
        window.blit(evil_can_images[i % 2], evil_can_rects[i])
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    instructions1 = font.render("Collect food for the food drive. Each fruit is worth 1 point. Avoid collecting ", True, (0, 0, 0))
    instructions2 = font.render("plastic items, those will subtract 5 points. Missing a can will also subtract 1 point.", True,
                                (0, 0, 0))

    window.blit(score_text, (10, 10))
    window.blit(instructions1, (200, 10))
    window.blit(instructions2, (200, 30))

    pygame.display.update()


# Set up for the game
pygame.init()
pygame.display.set_caption("Can Catch LMUHacks 2023")

# Variables
WIDTH = 900
HEIGHT = 700
FPS = 60
B_SPEED = 15
score = 0

# Window
window = pygame.display.set_mode((WIDTH, HEIGHT))
score_font = pygame.font.Font(None, 36)
font = pygame.font.Font(None, 26)

# clock
clock = pygame.time.Clock()

# Load images
collection_basket = pygame.image.load("Cart.png")
collection_basket = pygame.transform.scale(collection_basket, (150, 150))

# Banana
banana = pygame.image.load("Banana.gif")
banana = pygame.transform.scale(banana, (75, 75))
banana2 = pygame.image.load("Banana2.png")
banana2 = pygame.transform.scale(banana2, (75, 75))
banana3 = pygame.image.load("Banana3.png")
banana3 = pygame.transform.scale(banana3, (75, 75))
banana4 = pygame.image.load("Banana4.png")
banana4 = pygame.transform.scale(banana4, (75, 75))
banana5 = pygame.image.load("Banana5.png")
banana5 = pygame.transform.scale(banana5, (75, 75))
banana6 = pygame.image.load("Banana6.png")
banana6 = pygame.transform.scale(banana6, (75, 75))
banana7 = pygame.image.load("Banana7.png")
banana7 = pygame.transform.scale(banana7, (75, 75))
banana8 = pygame.image.load("Banana8.png")
banana8 = pygame.transform.scale(banana8, (75, 75))
# sort the fruits into a list
can_images = [banana, banana2, banana3, banana4, banana5, banana6, banana7, banana8]

# Bottle
bottle = pygame.image.load("Bottle.gif")
bottle = pygame.transform.scale(bottle, (75, 75))
bottle2 = pygame.image.load("Bottle2.png")
bottle2 = pygame.transform.scale(bottle2, (75, 75))
bottle3 = pygame.image.load("Bottle3.png")
bottle3 = pygame.transform.scale(bottle3, (75, 75))
bottle4 = pygame.image.load("Bottle4.png")
bottle4 = pygame.transform.scale(bottle4, (75, 75))
bottle5 = pygame.image.load("Bottle5.png")
bottle5 = pygame.transform.scale(bottle5, (75, 75))
bottle6 = pygame.image.load("Bottle6.png")
bottle6 = pygame.transform.scale(bottle6, (75, 75))
bottle7 = pygame.image.load("Bottle7.png")
bottle7 = pygame.transform.scale(bottle7, (75, 75))
bottle8 = pygame.image.load("Bottle8.png")
bottle8 = pygame.transform.scale(bottle8, (75, 75))
# sort the fruits into a list
evil_can_images = [bottle, bottle2, bottle3, bottle4, bottle5, bottle6, bottle7, bottle8]

# Set up the basket
basket_rect = collection_basket.get_rect()
basket_rect.bottom = HEIGHT - 20

# Set up the cans
cans = []
can_rects = []
can_speeds = []
for i in range(5):  # 5 cans on the screen at a time
    can = random.choice(can_images)
    can_rect = can.get_rect()
    can_rect.left = random.randint(0, WIDTH - can_rect.width)
    can_rect.top = random.randint(-HEIGHT, -can_rect.height)
    can_speed = random.randint(3, 8)
    cans.append(can)
    can_rects.append(can_rect)
    can_speeds.append(can_speed)

# Set up the evil cans (they subtract points)
evil_can_rects = []
evil_can_speeds = []
for i in range(2):  # 2 evil cans on the screen at a time
    evil_can = random.choice(evil_can_images)
    evil_can_rect = evil_can.get_rect()
    evil_can_rect.left = random.randint(0, WIDTH - evil_can_rect.width)
    evil_can_rect.top = random.randint(-HEIGHT, -evil_can_rect.height)
    evil_can_speed = random.randint(3, 8)
    evil_can_rects.append(evil_can_rect)
    evil_can_speeds.append(evil_can_speed)

# game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_basket()
    drop_cans()
    drop_evil_cans()
    update_screen()

    # Wait for the next frame
    clock.tick(FPS)
