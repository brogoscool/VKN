import math
x = float(input("Значення аргументу:"))
y=math.pow(3, x-4)+math.log1p(x)+math.log10(x)      
y1=math.pow(x,2)+math.sin(2*x)  
y2=2+(2.7*(x ** 2))

if x>=6:
    print(y)
elif x > -1:
    print(y1)
else:
    print(y2)


