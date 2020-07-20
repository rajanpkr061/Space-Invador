import pygame
#initialize the pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))
#tittle and icon

pygame.display.set_caption("Space war\n Author:Aman")
icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

playerX_change = 0
#playerY_change = 0


def player(x,y):
	screen.blit(playerImg,(x,y))


#game loop
running = True

while running:
        
	#           R  G  B
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		#if a keystroke is pressed whether its is right or left
		if event.type == pygame.KEYDOWN:
			print("kystroke pressed")
			if event.key == pygame.K_LEFT:
				playerX_change = 0.3
				print("left key pressed")
			if event.key == pygame.K_RIGHT:
				print("right key pressed")
				playerX_change = 0.3
		if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0.3
			  	print("keystroke released")
 

        playerX  +=  playerX_change
	player(playerX,playerY)	
	pygame.display.update()
