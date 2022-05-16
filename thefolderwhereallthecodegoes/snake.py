import pygame
import random
class Snake:
    def __init__(self, x, y, speed, screen,width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.screen = screen
        self.direction = 1
        self.size = 30
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
        self.bodyParts = []
        self.width = width
        self.height = height
        self.dead = False
        self.speedTwo = speed
        while len(self.bodyParts)<20:
            self.bodyParts.append((x,y))
    #0--up ; 1-- right; 2-- down; 3-- left
    def draw(self):
        self.rect = pygame.Rect(self.x,self.y,self.speed,self.speed)
        if self.direction == 0:
                    self.y -= self.speed
            # for bodyPart in self.bodyParts:
        elif self.direction == 1:
            self.x += self.speed
        elif self.direction == 2:
            self.y += self.speed
        else:
            self.x -= self.speed
        if self.x>self.width or self.x<0 or self.y<0 or self.y>self.height:
            self.dead=True
            self.speed = 0

        self.bodyParts.pop()
        self.bodyParts.insert(0,(self.x,self.y))
        for i in range(len(self.bodyParts)):
            pygame.draw.circle(self.screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), self.bodyParts[i], self.size)
        self.check_collisions()
    def grow(self):
        i=0
        while i<3:
            i=i+1
            self.bodyParts.append(self.bodyParts[-1])

    def check_collisions(self):
        head = self.bodyParts[0]
        for bodyPart in self.bodyParts:
            if head[0]-bodyPart[0] < self.size*2 and head[1]-bodyPart[1] < self.size*2:
                print(str(random.randint(1,1000)))

    def aliveAgain(self):
        self.dead = False
        self.speed = self.speedTwo
        self.x = self.width // 2
        self.y = self.height // 2



