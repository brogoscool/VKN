import math 
x=float(input("Введіть значення a:"))
y=float(input("Введіть значення b:"))
h=float(input("Введіть значення h:"))
spisok=[]
while x<10:    
    y=(1/math.pow(x,2)+1)+math.pow(x,2)   
    spisok.append(y)     
    x=x+h 

print(spisok)