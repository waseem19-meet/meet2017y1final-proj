import turtle

turtle.hideturtle()

turtle.register_shape("lava.gif")

turtle.shape("lava.gif")

size_x =1000

size_y =700

turtle.setup(size_x,size_y)

lava_height = 40

turtle.penup()

turtle.goto(-size_x/2+500,-size_y/2+lava_height)

turtle.showturtle()

##if player.pos() <= -size_y/2+lava_height:


##    print('game over')


##    quit()
