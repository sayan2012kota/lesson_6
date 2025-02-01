import pgzrun
from random import randint
import time

TITLE = "Bumblebee Game"
HEIGHT = 500
WIDTH = 600

score = 0
game_over = False

bee = Actor("bee")
bee.pos = 100,100

flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.blit("background" , (0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score:" + str(score) , color= "black", topleft=(10,10))

#when you miss the flower its game over
    if game_over:
        screen.fill("pink")
        screen.draw.text("Game over : " + str(score), middtop= (WIDTH/2 , 10), fontsize= 30 , color="red" )

def place_flower():
    x = randint(70 , (WIDTH -70 ))
    y = randint (70, (HEIGHT -70 ))



def gameOver():
    global game_over
    game_over = True

    def update ():
        global score
        if keyboard.left:
            bee.x = bee.x - 2
        
        if keyboard.right:
            bee.x = bee.x + 2

        if keyboard.up:
            bee.y = bee.y + 2
            
        if keyboard.down:
            bee.y = bee.y - 2


    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score = score + 10
        place_flower()





clock.schedule(gameOver, 60 )






pgzrun.go()