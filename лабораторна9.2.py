from array import *
A1=[]
A2=[]
for i in range(200):
    if i%4==0:
        A1.append(i)
m4=set(A1)
for i in range(200):
    if i%3==0:
        A2.append(i)
m3=set(A2)
 
m12=set()
m12=m4, m3 
print(m4)
print(m3)



