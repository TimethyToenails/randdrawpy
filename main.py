import turtle               # allows us to use the turtles library
import random

wn = turtle.Screen()        # creates a graphics window
t = turtle.Turtle()      # create a turtle named t
wn.screensize(canvwidth=10, canvheight=10, bg=None)

while(True):
	print('start')
	movement_amount = random.randint(0, 4)
	movment = random.randint(0, 4)
	if movment == '0':
		t.down(movement_amount)
		print('moving down')
	elif movment == '1':
		t.forward(movement_amount)
		print('moving forward')
	elif movment == '2':
		t.left(movement_amount)
		print('turning lef')
	elif movment == '3':
		t.right(movement_amount)
		print('turning right')
