import turtle
import random
SIZE_X=1000
SIZE_Y=700
turtle.setup(SIZE_X,SIZE_Y)
turtle.shape('square')

stamp_list=[]
turtle.hideturtle()

cloud=turtle.clone()


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




    

##    cloud.goto(x,y)
##    cloud_pos.append((x,y))
##    new_stamp=cloud_stamp()
##    cloud_stamp.append(new_stamp)



