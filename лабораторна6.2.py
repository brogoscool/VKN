import math 
x=float(input()) 
y=float(input()) 
h=float(input()) 
while x<10:     
    y=(1/math.pow(x,2)+1)+math.pow(x,2)  
    print("x=%.1f y=%.3f"%(x,y)) 
    x=x+h