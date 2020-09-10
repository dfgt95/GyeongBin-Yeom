import turtle as t

x = 0
y = 0

while ( y <= 500 ):
	t.forward(300)
	if ( y ==300 ):
            t.up()
            t.left(90)
            t.goto(0,0)
            t.down()
            while ( x <= 300 ):
                t.forward(300)
                t.up()
                x += 60
                t.goto(x,0)
                t.down()
	t.up()
	y += 60
	t.goto(0,y)
	t.down()
    
t.exitonclick()
