import turtle

size_x =1000

size_y =700
turtle.setup(size_x,size_y)
lava_height = 50

turtle.penup()

turtle.goto(-size_x/2 ,-size_y/2+lava_height)

turtle.pendown()

turtle.goto(size_x/2,-size_y/2+lava_height)

##if player.pos() <= -size_y/2+lava_height:
##    print('your player is barbequed now')
##    print('game over')
##    print('all rights belong to team miaw :)')
##    quit()

    
