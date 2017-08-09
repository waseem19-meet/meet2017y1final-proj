import turtle
import random

#-------------VARIABLES------------
SIZE_X=1000
SIZE_Y=700
turtle.setup(SIZE_X,SIZE_Y)
turtle.shape('square')
turtle.bgcolor("turquoise")

SQUARE_SIZE=20
START_LENGTH=7
player=turtle.clone()
turtle.register_shape("player.gif")
turtle.register_shape("cloud.gif")
player.shape("player.gif")
#put the player gif in the row above .don't forget to define it
turtle.hideturtle()
pos_list=[]
lava_hight=20
turtle.penup()
turtle.goto(-SIZE_X/2,-SIZE_Y/2+lava_hight)
turtle.pendown()
turtle.goto(SIZE_X/2,-SIZE_Y/2+lava_hight)

player.penup()
player.goto(-SIZE_X/2+110,-SIZE_Y/2+lava_hight+35)


stamp_list=[]
turtle.hideturtle()

cloud=turtle.clone()
cloud.shape('cloud.gif')
cloud.penup()

##cloud_pos=[]
##num_clouds=5
##cloud_space=(SIZE_Y-START_LENGTH-TOP)/(num_clouds+1)
cloud.penup()
cloud.goto(-300,-300)
cloud.showturtle()
cloud.stamp()
cloud.goto(-200,-200)
cloud.stamp()
cloud.goto(-100,-100)
cloud.stamp()
cloud.goto(0,0)
cloud.stamp()
cloud.goto(100,100)
cloud.stamp()
cloud.goto(200,200)
cloud.stamp()

UP_ARROW = "Up"
RIGHT_ARROW='Right'
TIME_STEP = 1000
SPACEBAR = "space"
UP = 0
RIGHT=1
UP_EDGE=250
jump_speed=100
direction=UP

cloud_pos_list=[(-300,-300),(-200,-200),(-100,-100),(0,0),(100,100),(200,200)]



#-----------FUNCTIONS-------------
def move_player():
    my_pos=player.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==UP:
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        #turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        
        #turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0],player.pos()[1]+SQUARE_SIZE),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0]+SQUARE_SIZE,player.pos()[1]),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0]+SQUARE_SIZE,player.pos()[1]),jump_speed)
        #turtle.ontimer(player.goto(player.pos()[0]+SQUARE_SIZE,player.pos()[1]),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0]+SQUARE_SIZE,player.pos()[1]),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0]+SQUARE_SIZE,player.pos()[1]),jump_speed)
        turtle.ontimer(player.goto(player.pos()[0]+SQUARE_SIZE,player.pos()[1]),jump_speed)
        
        
        
        
        print("you moved up")
        
    if direction==RIGHT:
        player.goto(x_pos+SQUARE_SIZE, y_pos)
        print('YOU MOVED RIGHT')
        
    if player.pos()[1]<=-SIZE_Y/2+lava_hight:
        print("game over!!!")
        quit()

def up():
    global direction
    direction=UP
    move_player()
    print("you pressed up")

def right():
    global direction
    direction=RIGHT
    move_player()
    print('you pressed right')


    
#--------------MAIN PROGRAM------------

for i in range(START_LENGTH):
    x_pos=player.pos()[0]
    y_pos=player.pos()[1]
   #x_pos+=SQUARE_SIZE
    my_pos = (x_pos,y_pos)
    player.goto(x_pos,y_pos)
    pos_list.append(my_pos)





##
##if direction==UP:
##    cloud.stamp.goto(x-100,y-100)






    

##    cloud.goto(x,y)
##    cloud_pos.append((x,y))
##    new_stamp=cloud_stamp()
##    cloud_stamp.append(new_stamp)

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()



