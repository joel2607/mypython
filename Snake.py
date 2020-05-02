import pygame
import time
import random
import tkinter as tk


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

###TKINTER###


def darkmode():
    return "dm"
    
def lightmode():
    return "lm"
    
def init():
    win.destroy()
    win.quit()

    
win = tk.Tk()
win.title("Snake")

mode = tk.Frame()
modetxt = tk.Label(master = mode, text = 'Select Colour Scheme')
dark = tk.Button(master = mode, text = 'DARK MODE', bg = 'black', fg = 'yellow', command = darkmode)
light = tk.Button(master = mode, text = 'LIGHT MODE', bg = 'white', fg = 'green',command = lightmode)

mode.pack()
modetxt.pack()
dark.pack()
light.pack()

snake_speed = 30

def veryslowbutton():
    global snake_speed
    snake_speed = 10   
def slowbutton():
    global snake_speed
    snake_speed = 20
def mediumbutton():
    global snake_speed
    snake_speed = 30
def fastbutton():
    global snake_speed
    snake_speed = 40
def veryfastbutton():
    global snake_speed
    snake_speed = 50

speed = tk.Frame()
speedtxt = tk.Label(speed, text = 'Select Speed of Snake')
veryslow = tk.Button(speed, text = 'Very Slow', command = veryslowbutton)
slow = tk.Button(speed, text = 'Slow', command = slowbutton)
medium = tk.Button(speed, text = 'Medium', command = mediumbutton)
fast = tk.Button(speed, text = 'Fast', command = fastbutton)
veryfast = tk.Button(speed, text = 'Very Fast', command = veryfastbutton)

speed.pack()
speedtxt.pack()
veryslow.pack()
slow.pack()
medium.pack()
fast.pack()
veryfast.pack()




butt = tk.Button(win, text = 'Play',bg = 'blue', fg = 'white', command = init)
butt.pack()

win.mainloop()

print(snake_speed)

###PYGAME###


pygame.init()

if darkmode() == "dm":
    snakecolor = blue
    bgcolor = black
    msgcolor = red
    scorecolor = green
    foodcolor = yellow
else:
    snakecolor = black
    bgcolor = white
    msgcolor = red
    scorecolor = blue
    foodcolor = green


dis_width = 600
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10

 
font_style = pygame.font.SysFont("bahnschrift", 35)

def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, scorecolor)
    dis.blit(value, [0, 0])
     
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snakecolor, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            
            message("You Lost! Press C-Play Again or X-Quit", msgcolor)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(bgcolor)
        pygame.draw.rect(dis, foodcolor, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake-1)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()