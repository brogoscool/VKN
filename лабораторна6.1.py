import math 
x=float(input("Введіть змінну a:")) 
b=float(input("Введіть змінну b:")) 
h=float(input("Введіть змінну h:")) 
for i in range(5):
    if x > b:
        break 
    y=(1/math.pow(x,2)+1)+math.pow(x,2)  
    print("x=%.1f y=%.3f"%(x,y)) 
    x=x+h