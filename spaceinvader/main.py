import pygame
import random
import math
from pygame import mixer
import time


start = time.time()
# initialize the pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")

# background sound
mixer.music.load("TheFatRat_-_Unity(256k)_copy1.wav")
mixer.music.play(-1)


# tittle and icon
pygame.display.set_caption("Space war\n Author:Aman")
icon = pygame.image.load("launch.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("player.png")
playerX = 350
playerY = 530
counter = 0
playerX_change = 0
playerY_change = 0
k = 5

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy1.2.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 70))
    enemyX_change.append(1)
    enemyY_change.append(30)

# ready u cant use the bullet on the screen
# moving thr bullet is currently moving

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
# counter = 0
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# score

score = 0
font = pygame.font.Font("funky.ttf", 28)
textX = 10
textY = 10


# game over text
over = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    scoref = font.render("Score :" + str(score), True, (255, 255, 255))
    screen.blit(scoref, (x, y))


"""def playing(x,y):
    timef = 0
    time = font.render("Time :" + str(timef), True,(255,255,255))
    screen.blit(time,(x , y))"""


def player(x, y):
    screen.blit(playerImg, (x, y))


def game_over_text():
    over_text = over.render("GAME OVER!!!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def enemy(x, y):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 15, y + 12))


def isCollison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True

while running:
    #           R  G  B
    screen.fill((0, 0, 0))
    # background  image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if a keystroke is pressed whether its is right or left
        if event.type == pygame.KEYDOWN:
            print("kystroke pressed")
            if event.key == pygame.K_LEFT:
                playerX_change -= k
                print("left key pressed")
            if event.key == pygame.K_RIGHT:
                print("right key pressed")
                playerX_change = k

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
                    bullet_sound = mixer.Sound("Fireball+1_copy.wav")
                    bullet_sound.play()

            if event.key == pygame.K_UP:
                playerY_change -= k
            if event.key == pygame.K_DOWN:
                playerY_change = k
        if event.type == pygame.KEYUP:
            if (
                event.key == pygame.K_LEFT
                or event.key == pygame.K_RIGHT
                or event.key == pygame.K_UP
                or event.key == pygame.K_DOWN
            ):
                playerX_change = 0
                playerY_change = 0
                print("keystroke released")
    playerX += playerX_change
    playerY += playerY_change
    if playerX >= 736:
        playerX = 736
    if playerX <= 0:
        playerX = 0
    counter += 1

    # enemy movement
    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 350:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]

        if enemyX[i] >= 736:
            enemyX_change[i] = -1.0
            enemyY[i] += enemyY_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 1.0
            enemyY[i] += enemyY_change[i]

            # check if collison occured or not
        collison = isCollison(enemyX[i], enemyY[i], bulletX, bulletY)
        if collison:
            explosion_sound = mixer.Sound("enemyblast_copy.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 730)
            enemyY[i] = random.randint(50, 70)

        enemy(enemyX[i], enemyY[i])
    # bullet movement
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # playing(100,100)
    show_score(textX, textY)
    player(playerX, playerY)
    print(playerX, playerY, end="--------  ")
    print(counter)
    pygame.display.update()

