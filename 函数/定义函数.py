def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
age = 18
if age >= 18:
    pass

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)

import math
def quadratic(a,b,c):
	if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
		raise TypeError('bad operand type')
	if b*b -4*a <0:
		return "方程无解"
	elif a != 0:
		x = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
		y = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
		return x,y
	elif b != 0:
		return -c / b
	elif c != 0:
		return "方程无解"
	else:
		return None
print(quadratic(1,2,1))