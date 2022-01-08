def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    while wall_on_right():
        if wall_in_front(): 
            turn_left()
    
        else:
            move()
    if right_is_clear() and not at_goal():
        turn_right()
        move()