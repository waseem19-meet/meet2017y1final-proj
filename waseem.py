import turtle
import random
score=0
i=0
SIZE_X= 1000
SIZE_Y= 700
turtle.setup(SIZE_X,SIZE_Y)
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
food_pos_list=[(-300,-280),(-200,-180),(-100,-80),(0,20),(100,120),(200,220)]
food_shape_list = ["pizza.gif", "cake.gif", "cherry.gif", "chips.gif", "dounat.gif", "hamburger.gif"]

for pos in food_pos_list:
    food.shape(food_shape_list[i])
    food.goto(pos)
    stamp1=food.stamp()
    food_stamp_list.append(stamp1)
    i+=1


food.showturtle()

if player.pos in stamp_list:
    food.clearstamp()
    score= score+1
    turtle.goto(-450,300)
    turtle.write("your score is: "+score,font=("Arial","20","normal"))

    



    
    

