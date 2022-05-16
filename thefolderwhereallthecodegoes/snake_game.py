# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
from food import Food
from snake import Snake
pygame.init()
white = (255,255, 255)
pink = (255, 192, 203)
blue = (0, 0, 20)
width = 1000
height = 500
font = pygame.font.Font('freesansbold.ttf', 100)
boundries = font.render('Game Over', True, blue, pink)
boundriesRect = boundries.get_rect()
boundriesRect.center = (width/2,height/4)
#play again?
font = pygame.font.Font('freesansbold.ttf', 100)
playAgain = font.render('Play Again ??', True, blue, pink)
playAgainRect = playAgain.get_rect()
playAgainRect.center = (width/2,height/2)
font = pygame.font.Font('freesansbold.ttf', 75)
response1 = font.render("yes space", True, pink)
response2 = font.render ("no escape", True, pink, blue)
response1Rect = response1.get_rect()
response2Rect = response2.get_rect()
response1Rect.center = (width/2, height*0.95)
response2Rect.center = (width/2, height*0.8)


# Set up the drawing window
screen = pygame.display.set_mode([width, height])
snake = Snake(width//2, height//2, 4, screen, width, height)
food = Food(width//2,height//2,screen)

#food collide with snake
def collide():
    if snake.rect.colliderect(food.rect):
        return True
    else:
        return False
# Run until the user asks to quit
running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 0
            if event.key == pygame.K_RIGHT:
                snake.direction = 1
            if event.key == pygame.K_DOWN:
                snake.direction = 2
            if event.key == pygame.K_LEFT:
                snake.direction = 3
            if event.key == pygame.K_SPACE:
                snake.dead == False
                snake.aliveAgain()
            if event.key == pygame.K_ESCAPE and snake.dead == True:
                running = False


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    snake.draw()
    food.draw()
    if collide() == True:
        food.x = random.randint(0,width)
        food.y = random.randint(0,height)
        snake.grow()


# Flip the display
    if snake.dead == True:
        screen.blit(boundries, boundriesRect)
        screen.blit(playAgain,playAgainRect)
        screen.blit(response1,response1Rect)
        screen.blit(response2,response2Rect)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()