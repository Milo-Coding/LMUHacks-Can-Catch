"""
Program Description: A Fruit Catch type game created for LMUHacks 2023 and visually themed to promote food drives
Author: Milo Fritzen
Date: 4/15/2023
References:
Collaborators: Chris Beaudoin
"""

# NOTE: I used the word cans in my variable names but the actual sprites include other non-perishable items

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

        if evil_can_rects[i].colliderect(basket_rect):
            # Evil can caught
            evil_can_image = random.choice(evil_can_images)
            evil_can_rects[i] = evil_can_image.get_rect()
            evil_can_rects[i].left = random.randint(0, WIDTH - evil_can_rects[i].width)
            evil_can_rects[i].top = random.randint(-HEIGHT, -evil_can_rects[i].height)
            evil_can_speeds[i] = random.randint(3, 8)
            score -= 5


def update_screen():
    # Update the screen
    window.fill((255, 255, 255))
    window.blit(collection_basket, basket_rect)
    for i in range(len(can_rects)):
        window.blit(can_images[i % 2], can_rects[i])
    for i in range(len(evil_can_rects)):
        window.blit(evil_can_images[i % 2], evil_can_rects[i])
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))
    pygame.display.update()


# Set up for the game
pygame.init()
pygame.display.set_caption("Can Catch LMUHacks 2023")

# Variables
WIDTH = 1000
HEIGHT = 800
FPS = 60
B_SPEED = 10
score = 0

# Window
window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# clock
clock = pygame.time.Clock()

# Load images
collection_basket = pygame.image.load("can1.png")

can1_image = pygame.image.load("can1.png")
can2_image = pygame.image.load("can1.png")
# sort the fruits into
can_images = [can1_image, can2_image]

evil_can1_image = pygame.image.load("can1.png")
evil_can2_image = pygame.image.load("can1.png")
# sort the fruits into
evil_can_images = [evil_can1_image, evil_can2_image]

# Set up the basket
basket_rect = collection_basket.get_rect()
basket_rect.bottom = HEIGHT - 10

# Set up the cans
can_rects = []
can_speeds = []
for i in range(5):  # 5 cans on the screen at a time
    can = random.choice(can_images)
    can_rect = can.get_rect()
    can_rect.left = random.randint(0, WIDTH - can_rect.width)
    can_rect.top = random.randint(-HEIGHT, -can_rect.height)
    can_speed = random.randint(3, 8)
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
