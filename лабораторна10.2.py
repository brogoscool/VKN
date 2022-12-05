import os 
dir = os.path.abspath(os.curdir)
print(dir)
a = os.path.basename(__file__)
b = os.path.abspath(__file__).replace(a, '')
print(b)
os.rename("start.txt", "fin.txt")