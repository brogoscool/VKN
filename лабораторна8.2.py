from array import *
import numpy as np
import random
masivA=array('i',[0,0,0,0,0,0,0,0,0,0,0,0]) 
for i in range (12):        
    masivA[i]=random.randint(1, 24)
print(masivA)
i=0
masivB=np.zeros((3,4))
for k in range(3):     
    for j in range (4): 
        masivB[k][j]=masivA[i]
        i=i+1
print(masivB)