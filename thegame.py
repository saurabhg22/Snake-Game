import pygame
import time
import pickle
import random
pygame.init()

light_green = (191,248,22)
yellow=(255,245,62)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green = (0,155,0)
grey=(57,89,73)
start_length =5
display_width=800
display_height=600
fps=10
block_size=20
apllethickness=30

high_score = 0
scorefile = open('save.p', 'r')
high_score = int(scorefile.read())
scorefile.close()
img = pygame.image.load('head.jpg')
img2 = pygame.image.load('apple.jpg')
icon = pygame.image.load('icon.jpg')
tail = pygame.image.load('tail.jpg')
direction = "right"
direction2 = "right"
gd=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither")
pygame.display.set_icon(icon)
clock=pygame.time.Clock()

def pause():
    paused = True
    if paused == True:
        msgtoscrn("Paused",black,-100,100)
        msgtoscrn("Press C to continue or Q to exit",black)
        pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    intro=False
        gd.fill(white)
        
        imgrect = icon.get_rect()
        imgrect.center = display_width/2,display_height/2-150
        gd.blit(icon,imgrect)
        msgtoscrn("Welcome to Slither",green,10,80)
        msgtoscrn("Objective of the Game is to eat Red Apples",black,80,25)
        msgtoscrn("The more Apples you eat, the longer you get",black,120,25)
        msgtoscrn("If you run into yourself, or the edges,you will die",black,160,25)
        msgtoscrn("Press C to continue, P to pause, or Q to exit.",black,210,35)
        pygame.display.update()
        clock.tick(5)

def snake(block_size,snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img,90)
    elif direction == "up":
        head = pygame.transform.rotate(img,180)
    elif direction == "left":
        head = pygame.transform.rotate(img,270)
    elif direction == "down":
        head = img
    if len(snakelist)!=1:
        if snakelist[1][2] =="right":
            Tail = pygame.transform.rotate(tail,270)
        elif snakelist[1][2] =="up":
            Tail = tail
        elif snakelist[1][2] =="left":
            Tail = pygame.transform.rotate(tail,90)
        elif snakelist[1][2] =="down":
            Tail = pygame.transform.rotate(tail,180)
    font = pygame.font.SysFont("comicsansms",25)
    screen_score = font.render("Score: " + str(score),True,black)
    screen_high_score = font.render("High Score: " + str(high_score),True,black)
    
    gd.blit(screen_score,(0,0))
    gd.blit(screen_high_score,(display_width-190,0))
    
    for xny in snakelist[:-1]:
        if len(snakelist)!=1:
            pygame.draw.rect(gd,green,[xny[0],xny[1],block_size,block_size])
    if len(snakelist)!=1:
        gd.blit(Tail,(snakelist[0][0],snakelist[0][1]))
    gd.blit(head,(snakelist[-1][0],snakelist[-1][1]))
        
def msgtoscrn(msg,color,y_displace=0,size=25,x_displace=0):
    font = pygame.font.SysFont("comicsansms",size)
    screen_text = font.render(msg,True,color)
    textrect = screen_text.get_rect()
    textrect.center = (display_width/2) + x_displace,(display_height/2) + y_displace
    gd.blit(screen_text,textrect)
def game():
    m = 1
    global high_score
    global score
    score = 0
    global direction
    direction = "right"
    snakelist=[]
    snakelength=start_length
    ge = False
    go = False
    lead_x=display_width/2
    lead_y=display_height/2
    xc=20
    yc=0
    randapllex = random.randrange(0,display_width-apllethickness)
    randaplley = random.randrange(37,display_height-apllethickness)
    while not ge:

        if go == True:
            msgtoscrn("GAME OVER",black,-50,80)
            msgtoscrn("Press C to continue or Q to exit.",red,50,25)
            pygame.display.update()
        while go == True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key==pygame.K_c:
                        game()
        while go == False:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    ge=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT and direction != "right":
                        xc=-block_size
                        yc=0
                        direction = "left"
                    elif event.key==pygame.K_RIGHT and direction != "left":
                        xc=block_size
                        yc=0
                        direction = "right"
                    elif event.key==pygame.K_UP and direction != "down":
                        yc=-block_size
                        xc=0
                        direction = "up"
                    elif event.key==pygame.K_DOWN and direction != "up":
                        yc=block_size
                        xc=0
                        direction = "down"
                    elif event.key == pygame.K_p:
                        pause()
            lead_x+=xc
            lead_y+=yc
            if lead_x >=display_width or lead_x<0 or lead_y >=display_height or lead_y<37:
                go=True
                break
            gd.fill(yellow)
            gd.blit(img2,(randapllex,randaplley))
          
            
            while m <= start_length:
                snakehead = []
                snakehead.append(lead_x-(start_length-m+1)*block_size)
                snakehead.append(lead_y)
                snakehead.append(direction)
                snakelist.append(snakehead)
                m+=1
            snakehead=[]
            snakehead.append(lead_x)
            snakehead.append(lead_y)
            snakehead.append(direction)
            snakelist.append(snakehead)
            
            if len(snakelist)>snakelength:
                del snakelist[0]
            for each in snakelist[:-1]:
                if each[0]==snakehead[0] and  each[1]==snakehead[1]:
                    go=True
            
            if go ==False:
                pygame.draw.rect(gd,light_green,[0,0,display_width,35])
                snake(block_size,snakelist)
                pygame.draw.rect(gd,grey,[0,35,display_width,2])
            
            if lead_x + block_size>= randapllex and lead_x <= randapllex+apllethickness:
                if lead_y + block_size>= randaplley and lead_y <= randaplley+apllethickness:
                    randapllex = random.randrange(0,display_width-apllethickness)
                    randaplley = random.randrange(37,display_height-apllethickness)
                    score+=1
                    snakelength+=1
                    if score > high_score:
                        high_score+=1
            pygame.display.update()
            clock.tick(fps)
     
        scorefile = open('save.p', 'w')
        scorefile.write(str(high_score))
        scorefile.close()        
    pygame.mixer.quit()       
    pygame.quit()
    quit()

game_intro()
game()      
