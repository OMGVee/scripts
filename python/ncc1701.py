#!/usr/bin/env python
x, y, speed = 0, 0, 0
print("(%s, %s) # Begin with original position" % (x,y))
while True: #main inf loop of the simulation, don't forget to exit with break
    cmd = input()
    if cmd == 'w':
        speed += 1
        if speed > 5:
            speed = 5
            print("maximum speed")
        y += speed
        print("(%s, %s) # W increases the speed to %s and moves forward." % (x,y,speed))
    elif cmd == 'a':
        x -= 1
        y += speed
        if x < -5:
            print("wrong trajectory")
        print("(%s, %s) # A moves the ship left and forward." % (x,y))
    elif cmd == 'd':
        x += 1
        y += speed
        if x > 5:
            print("wrong trajectory")
        print("(%s, %s) # D moves the ship right and forward." % (x,y))
    elif cmd == 's':
        speed -= 1
        if speed < 1:
            speed = 1
            print("minimum speed")
        y += speed
        print("(%s, %s) # S decreases the speed to %s and moves forward." % (x,y,speed))

    if y > 250:
        print("contact lost")
        break
    if y == 250 and x == 0:
        print("(%s, %s) on the moon # Ship reaches the moon." %(x,y))
        break
