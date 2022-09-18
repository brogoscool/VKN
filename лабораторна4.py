import math
x=float(input())
y=(math.sin(x+4)-math.cos(3*x))/((5*x)**0.5+math.log(abs(x+4), 2))
print(y)


import math
k, a, b ,x=float(input()), float(input()), float(input()), float(input())
W=(6*k**3-math.sin(a)+(math.cos(b))**2)*(abs(b)**0.5+(math.e)**x/3*a**7)
print(W)