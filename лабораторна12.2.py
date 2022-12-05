import random
n=str(input("Слово= "))
r=random.choice("qwertyuiopasdfghjklzxcvbnm")
n=r.join(n)
def R():
    global n
    print("Змінене слово=", n)
    def R2():
        global n
        print("Друге змінене слово=", n[::2])
    R2()
R()

   