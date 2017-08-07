import turtle
import random
SIZE_X=800
SIZE_Y=600
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()
SQUARE_SIZE=20
START_LENGTH=7
player=turtle.clone()
player.shape("circle")
#put the player gif in the row above .don't forget to define it
turtle.hideturtle()
pos_list=[]
for i in range(START_LENGTH):
    x_pos=player.pos()[0]
    y_pos=player.pos()[1]
   #x_pos+=SQUARE_SIZE
    my_pos = (x_pos,y_pos)
    player.goto(x_pos,y_pos)
    pos_list.append(my_pos)

UP_ARROW = "Up"
TIME_STEP = 1000
SPACEBAR = "space"
UP = 0
UP_EDGE=250
jump_speed=100
direction=UP

def up():
    global direction
    direction=UP
    move_player()
    print("you pressed up")

turtle.onkeypress(up,UP_ARROW)
turtle.listen()
def move_player():
    my_pos=player.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==UP:
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]-SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]-SQUARE_SIZE),jump_speed)
        print("you moved up")
        


