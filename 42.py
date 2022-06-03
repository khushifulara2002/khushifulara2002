#find distance between two points

import math

p1x=float(input("enter the x coordinate of point 1   "))

p1y=float(input("enter the y coordinate of point 1    "))

p2x=float(input("enter the x coordinate of point 2     "))

p2y=float(input("enter the y coordinates of point 2     "))

x=math.pow((p2x-p1x),2)
y=math.pow((p2y-p1y),2)

distance=math.sqrt(x+y)
print(distance)
