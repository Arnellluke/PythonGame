import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

pygame.init()


GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


# window variables 
windowWidth = 800
windowHeight = 400

# Rectable variables
rectX = 200
rectY = 200
rectendX = 87
rectendY = 113

# playervariables 
playerSize = 20
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 0.0

jumpHeight = 20
moveSpeed = 1
maxSpeed = 10
gravity = 0.9


# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False

clock = pygame.time.Clock()
window = pygame.display.set_mode( (windowWidth,windowHeight) )

blob = pygame.image.load('images/christ.jpg')


xdirection = 1
ydirection = 1

def quitgame():
	pygame.quit()
	sys.exit()

def move():

	global playerX, playerY, playerVX, playerVY, haveJumped, gravity

	# Move left 
	if leftDown:
		#If we're already moving to the right, reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX	
		# Make sure our square doesn't leave our window to the left
		if playerX > 0:
			playerX += playerVX	

	# Move right
	if rightDown:
		# If we're already moving to the left reset the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Make sure our square doesn't leave our window to the right
		if playerX + playerSize < windowWidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Is our square in the air? Better add some gravity to bring it back down!
	if playerY < windowHeight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowHeight - playerSize
		gravity = 1.0

	playerY -= playerVY

	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1
	
	
	
while True:
	window.fill((0,0,0))
	rand = random.randint(0,3)
	
	
	##pygame.draw.rect(window, GREEN, (rectX, rectY, rectendX, rectendY))
	pygame.draw.rect(window, (255,0,0), (playerX, playerY, playerSize, playerSize))
	window.blit(blob,(rectX, rectY, rectendX, rectendY))
	
	if rectX < 0:
		xdirection = 1	
	if rectX > windowWidth - rectendX:
		xdirection = -1
	if rectY <  0:
		ydirection = 1
	if rectY > windowHeight - rectendY:
		ydirection = -1

	rectY += ydirection * rand
	rectX += xdirection * rand


	#rectX += random.randint(-25,25)
	#rectY += random.randint(-25,25)
	##rectendX += 1
	##rectendY += 1

	##pygame.draw.rect(window, GREEN, (rectX, rectY, rectendX, rectendY))
	
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			quitgame()
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitgame()
		

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed


	move()

	
	clock.tick(100)
	pygame.display.update()			
	

	
	
