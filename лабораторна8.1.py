from array import * 
import numpy as np 
import random
b=int(input("Межа масива: "))
c=int(input("Додане число: "))
masivN=array('i',[0,0,0,0,0,0,0,0,0,0]) 
for i in range (10):      
    masivN[i]=random.randint(0,b)
masivN.append(c)
N=np.sort(masivN)
print(N)