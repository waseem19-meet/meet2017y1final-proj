import turtle
import random
turtle.bgpic("sky.gif")
#-------------VARIABLES------------
score=0
SIZE_X=1000
SIZE_Y=700
turtle.setup(SIZE_X,SIZE_Y)
turtle.tracer(1,0)
turtle.shape('square')
##platform=turtle.clone()
##platform.shape('square')
##platform.penup()
##platform.goto(-350,-482)
##platform.pendown()
##platform.goto(-300,-482)
##platform.stamp()



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
turtle.register_shape('lava.gif')
lava=turtle.clone()
lava.penup()
lava.shape('lava.gif')
lava.showturtle()
lava.goto(0,-SIZE_Y/2+lava_hight)
turtle.penup()
turtle.goto(-SIZE_X/2,-SIZE_Y/2+lava_hight)
#turtle.pendown()
#turtle.goto(SIZE_X/2,-SIZE_Y/2+lava_hight)

player.penup()
player.goto(-SIZE_X/2+100,-SIZE_Y/2+lava_hight+40)


stamp_list=[]
turtle.hideturtle()
scoreboard=turtle.clone()
scoreboard.goto(-450,300)
scoreboard.write("your score is: "+str(0),font=("Arial","20","normal"))

cloud=turtle.clone()
cloud.shape('cloud.gif')
cloud.penup()

##cloud_pos=[]
##num_clouds=5
##cloud_space=(SIZE_Y-START_LENGTH-TOP)/(num_clouds+1)

cloud.penup()
cloud.showturtle()
cloud_pos_list=[]
cloud_stamp_list=[]
for num in range(-300, 200 + 1, 100):
    cloud.goto(num, num)
    cloud_pos_list.append(cloud.pos())
    cloud_stamp_list.append(cloud.stamp())
        
##cloud.goto(-300,-300)
##cloud.showturtle()
##cloud.stamp()
##cloud.goto(-200,-200)
##cloud.stamp()
##cloud.goto(-100,-100)
##cloud.stamp()
##cloud.goto(0,0)
##cloud.stamp()
##cloud.goto(100,100)
##cloud.stamp()
##cloud.goto(200,200)
##cloud_stamp_list.append(cloud.stamp()) 

UP_ARROW = "Up"
RIGHT_ARROW='Right'
LEFT_ARROW = 'Left'
TIME_STEP = 1000
SPACEBAR = "space"
UP = 0
RIGHT=1
LEFT=2
UP_EDGE=250
jump_speed=100
SQUARE_SIZE = 20
direction=UP

c = 50
d = 50
jump_x = [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
jump_y =[1,1,1,1,1,1,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]



#-----------FUNCTIONS-------------


##def move_clouds():
##    for index in range(len(cloud_pos_list)):
##        cloud_pos = cloud_pos_list[index]
##        cloud_stamp = cloud_stamp_list[index]
##        cloud.clearstamp(cloud_stamp)
##        cloud.goto(cloud_pos[0] + 100, cloud_pos[1])
##        cloud_pos_list.append(cloud_pos)
##        cloud_stamp_list.append(cloud.stamp())
##
##    for index in range(len(cloud_pos_list)):
##        cloud_pos = cloud_pos_list[index]
##        cloud_stamp = cloud_stamp_list[index]
##        cloud.clearstamp(cloud_stamp)
##        cloud.goto(cloud_pos[0] - 100, cloud_pos[1])
##        cloud_pos_list.append(cloud_pos)
##        cloud_stamp_list.append(cloud.stamp())
##
##    turtle.ontimer(move_clouds, 10000)
##move_clouds()
    

    
def move_player():
    global score
    my_pos=player.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==UP:
        success = False
        for i in range(len(jump_x)):
            print(i)
            a=jump_x[i]*SQUARE_SIZE
            b=jump_y[i]*SQUARE_SIZE
            turtle.ontimer(player.goto(player.pos()[0]+a,player.pos()[1]+b),jump_speed)
            new_pos=player.pos()
            for position in cloud_pos_list:
                if (new_pos[0]>=position[0]-c) and (new_pos[0]<=position[0]+c) and (new_pos[1]<=position[1]+d)and (new_pos[1]>=position[1]-d):
                    player.goto(new_pos[0],position[1]+d)
                    on_cloud=cloud_pos_list.index(position)
                    success=True
            if success:
                break
        if i == len(jump_x)-1:
            quit()
        print("you moved up")
        
    if direction==RIGHT:
        player.goto(x_pos+SQUARE_SIZE, y_pos)
        print('YOU MOVED RIGHT')
             
    if direction==LEFT:
        player.goto(x_pos-SQUARE_SIZE, y_pos)
        print('YOU MOVED LEFT')
        
    if player.pos() in food_pos_list:
        ind = food_pos_list.index(player.pos())
        food.clearstamp(food_stamp_list[ind])
        food_stamp_list.pop(ind)
        food_pos_list.pop(ind)
        score= score+1
        scoreboard.clear()
        scoreboard.write("your score is: "+str(score),font=("Arial","20","normal"))
    
    if player.pos()[1]<=-SIZE_Y/2+lava_hight:
        print("game over!!!")
        quit()

turtle.hideturtle()
turtle.register_shape("pizza.gif")
turtle.register_shape("cake.gif")
turtle.register_shape("cherry.gif")
turtle.register_shape("chips.gif")
turtle.register_shape("dounat.gif")
turtle.register_shape("hamburger.gif")

turtle.shape("triangle")
food=turtle.clone()
food.penup()
food_stamp_list=[]

food_pos=[]

food.penup()
##food_pos_list=[(-300,-250),(-200,-150),(-100,-50),(0,50),(100,150),(200,250)]
food_shape_list = ["pizza.gif", "cake.gif", "cherry.gif", "chips.gif", "dounat.gif", "hamburger.gif"]
food_pos_list = []
n=0
for pos in cloud_pos_list:
    food.shape(food_shape_list[n])
    food.goto(pos[0],pos[1]+50)
    food_pos_list.append((pos[0],pos[1]+50))
    stamp1=food.stamp()
    food_stamp_list.append(stamp1)
    n+=1


food.hideturtle()    

def left():
    global direction
    direction=LEFT
    move_player()
    print("you pressed up")

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
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)



    

turtle.listen()






<<<<<<< HEAD
=======



>>>>>>> 8e937dfc97ef04ba5255050185682f3d67223ac6
