# Simple pygame program

# Import and initialize the pygame library
import pygame
x=250
y=250
r=100
white = (255,255, 255)
pink = (255, 192, 203)
blue = (0, 0, 20)
width = 500
height = 500
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,

)


pygame.init()
pygame.mixer.init()

font = pygame.font.Font('freesansbold.ttf', 32)
question = font.render('Welcome To Your Survey', True, blue, pink)
questionRect = question.get_rect()
questionRect.center = (width/2,height/2)
response1 = font.render("Start :D", True, pink)
response2 = font.render ("ugh start...", True, pink, blue)
response1Rect = response1.get_rect()
response2Rect = response2.get_rect()
response1Rect.center = (width/2, height*0.9)
response2Rect.center = (width/2, height*0.8)
# Set up the drawing window
screen = pygame.display.set_mode([width, height])


# Run until the user asks to quit
questionNumber=0
def refreshText(qtext, r1text, r2text, questionNumber2):
    global questionNumber
    global question
    global response1
    global response2
    global questionRect
    global response1Rect
    global response2Rect
    question = font.render(qtext, True, pink)
    response1 = font.render(r1text, True, blue, white)
    response2 = font.render(r2text, True, blue, white)
    questionRect = question.get_rect()
    response1Rect = response1.get_rect()
    response2Rect = response2.get_rect()
    questionRect.center = (width // 2, height // 2)
    response1Rect.center = (width/2, height*0.8)
    response2Rect.center = (width/2, height*0.9)
    questionNumber = questionNumber2
running = True
answers = []
while running:
    pressedKeys = pygame.key.get_pressed()
    pressedMouse = pygame.mouse.get_pressed()


    if pressedKeys[K_LEFT]:
        x-= 1
    elif pressedKeys[K_DOWN]:
        y+= 1
    elif pressedKeys[K_UP]:
        y-= 1
    elif pressedKeys[K_ESCAPE]:
        r+=1
    elif pressedKeys[K_SPACE]:
        if r-1>=0:
            r-=1


    # Did the user click the window close button?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if questionNumber == 0:
                mouseposition = pygame.mouse.get_pos()
                if response1Rect.collidepoint(mouseposition):
                    print("chose response 2")
                    refreshText('is quarantine going well', "yes", "no- it's terrible", 1)
                    answers.append("1")
                    break
                elif response2Rect.collidepoint(mouseposition) :
                    print("chose response 1")
                    if response2Rect.collidepoint(mouseposition):
                        refreshText('are you happy rn', "I'm sad", "i guess", 2)
                        answers.append("2")
                        break
            elif questionNumber == 1:
                mouseposition = pygame.mouse.get_pos()
                if response1Rect.collidepoint(mouseposition):
                    refreshText('do you think everythings alright', 'yes', 'no!', 3)
                    answers.append("1")
                    break
                elif response2Rect.collidepoint(mouseposition) :
                    refreshText('hows summer', 'nice and smooth', 'pretty rough', 4)
                    answers.append("2")
                    break
            elif questionNumber == 2 :
                mouseposition = pygame.mouse.get_pos()
                if response1Rect.collidepoint(mouseposition):
                    refreshText('do you have company', 'yup', 'pretty much no', 5)
                    answers.append("1")
                    break
                elif response2Rect.collidepoint(mouseposition):
                    refreshText('describe your moods', 'they switch a lot', 'bubbly or rocky', 6)
                    answers.append("2")
                    break
            elif questionNumber == 3 :
                mouseposition = pygame.mouse.get_pos()
                if response1Rect.collidepoint(mouseposition):
                    answers.append("1")
                    questionNumber = questionNumber + 1
                elif response2Rect.collidepoint(mouseposition):
                    answers.append("2")
                    questionNumber = questionNumber + 1

            elif questionNumber == 4 :
                mouseposition = pygame.mouse.get_pos()
                if response1Rect.collidepoint(mouseposition):
                    answers.append("1")
                    questionNumber = questionNumber + 1
                elif response2Rect.collidepoint(mouseposition):
                    answers.append("2")
                    questionNumber = questionNumber + 1

            elif questionNumber == 5 :
                mouseposition = pygame.mouse.get_pos()
                if response1Rect.collidepoint(mouseposition):
                    answers.append("1")
                    questionNumber = questionNumber + 1
                elif response2Rect.collidepoint(mouseposition):
                    answers.append("2")
                    questionNumber = questionNumber + 1

            elif questionNumber == 6 :
                mouseposition = pygame.mouse.get_pos()
                if response1Rect.collidepoint(mouseposition):
                    answers.append("1")
                    questionNumber = questionNumber + 1
                elif response2Rect.collidepoint(mouseposition):
                    answers.append("2")
                    questionNumber = questionNumber + 1

            elif questionNumber == 7 :
                ones = answers.count("1")
                twos = answers.count("2")
                if ones > twos:
                    refreshText("i see- thank you", "well we'll callibrate results",  "thanks", 0)
                elif twos > ones:
                    refreshText("okay- looks like you're alright","thanks","see you later", 0)






    # Fill the background with white
    screen.fill((0, 255, 255))

    # Draw a solid blue circle in the center

    # Flip the display
    screen.blit(question, questionRect)
    screen.blit(response1, response1Rect)
    screen.blit(response2, response2Rect)
    pygame.display.flip()


# Done! Time to quit.
print(answers)
pygame.quit()