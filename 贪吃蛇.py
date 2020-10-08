import pygame,sys
import time


pygame.init()


screen = pygame.display.set_mode((800,600))
game_going = True

class juxing:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.color=[255,0,255]
    def draw(self):
        pygame.draw.rect(screen,self.color,[self.x,self.y,20,20],0)
        pygame.draw.rect(screen,[0,0,0],[self.x,self.y,20,20],1)
        
class Snake:
    def __init__(self):
        self.x=0
        self.y=300
        self.size=20
        self.headColor=[255,255,0]
        self.bodyColor=[255,0,255]
        self.direction="right"
        self.body=[]
        
        for x in range(10):
            self.body.append(juxing(self.x,self.y))
            self.y+=20
        self.y=300
    
        
    def draw(self): 
        self.body[0].color=self.headColor
        for ba in range(1,len(self.body)):
            self.body[ba].color=self.bodyColor
        for rect in self.body:
            rect.draw()
    def step(self):
        if self.direction=="top":
            self.y-=20
        elif self.direction=="down":
            self.y+=20
        elif self.direction=="left":
            self.x-=20
        elif self.direction=="right":
            self.x+=20
        self.body.insert(0,juxing(self.x,self.y))
        self.body.pop()
        
snake=Snake()

def game():
    snake.draw()
    snake.step()
lastTIme=time.time()
while game_going:
    now=time.time()
    if now-lastTIme>=0.5:
        screen.fill([0,0,0])
        game()
        lastTIme=now
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                snake.direction="top"
            if event.key==274:
                snake.direction="down"
            if event.key==276:
                snake.direction="left"
            if event.key==275:
                snake.direction="right"
        if event.type ==pygame.QUIT:
            game_going = False
        
        
        pygame.display.update()
pygame.quit()     
sys.exit()

