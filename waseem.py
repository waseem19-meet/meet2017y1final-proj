import turtle
import random
score=0
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
stamp_list=[]

food_pos=[]

food.penup()
food.shape("pizza.gif")
food.goto(-300,-295)
food.showturtle()
pizza=food.stamp()
stamp_list.append(pizza)
food.shape("cake.gif")
food.goto(-200,-195)
cake=food.stamp()
stamp_list.append(cake)
food.shape("cherry.gif")
food.goto(-100,-95)
cherry=food.stamp()
stamp_list.append(cherry)
food.shape("chips.gif")
food.goto(0,5)
chips=food.stamp()
stamp_list.append(chips)
food.shape("dounat.gif")
food.goto(100,95)
dounat=food.stamp()
stamp_list.append(dounat)
food.shape("hamburger.gif")
food.goto(200,195)
hamburger=food.stamp()
stamp_list.append(hamburger)

if player_pos in stamp_list:
    food.clearstamp()
    score= score+1
    turtle.goto(-450,300)
    turtle.write("your score is: "+score)
    



    
    

