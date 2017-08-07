import turtle
import random
SIZE_X=1000
SIZE_Y=3000
START_LENGTH=270
START_HEIGHT=50
TOP=20
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()
turtle.shape('square')
stamp_list=[]
cloud=turtle.clone() 
cloud_pos=[]
num_clouds=10
cloud_space=(SIZE_Y-START_LENGTH-TOP)/(num_clouds+1)


for num in range(num_clouds):
    x=-SIZE_X/2
    y=START_HEIGHT+(num+1)*cloud_space

    cloud.goto(x,y)
    cloud_pos.append((x,y))
    new_stamp=cloud_stamp()
    cloud_stamp.append(new_stamp)



