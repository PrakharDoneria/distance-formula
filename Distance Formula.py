from math import sqrt
x1 =int(input("Entre x1:"))
x2 =int(input("Entre x2:"))
y1 =int(input("Entre y1:"))
y2 =int(input("Entre y2:"))
#This would calculate the above
x = x2 - x1
X=x*x
y = y2 -y1
Y=y*y
new=X+Y
distance = sqrt(new)
print("Distance between two points will be", distance)
