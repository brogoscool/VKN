import random
import re
rk=int(input("Виберіть кількість символів= "))
rs="qwertyuiopasdfghjklzxcvbnm"
x='' 
n="0123456789"
rn=random.choice(n)+random.choice(n)
print(rn)

for i in range(rk):    
    y=random.choice(rs)                
    x=x+y 
    
def rndm(rk):                                  
    print(x)    
    def rndm1():
        r=re.sub(x[2:3], " ", x)
        r1=re.sub(x[5:6], " ", r)
        r2=re.sub(x[8:9], " ", r1)
        print("Остаточний результат="+r2.replace(" ", rn))
            
    rndm1()
    
rndm(rk)
         