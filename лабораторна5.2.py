import math
x=int(input("Значення х:"))
y=int(input("Значення у:"))
z=int(input("Знчаення z:"))
R=int(input("Значення радіуса:"))

a=math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)
b=math.pow(R, 2)
if a!=b:
    print("Error")
else:
    print("Done")
