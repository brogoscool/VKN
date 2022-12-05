import csv

Name1="1,2,3,4,5"
Name2=[int(input("1 день= ")), 
int(input("2 день= ")), 
int(input("3 день= ")), 
int(input("4 день= ")), 
int(input("5 день= "))]
for writer in Name1:
    with open("weather.csv", "w") as file:
        writer=csv.writer(file)
        writer.writerow((Name1, Name2))
mn=min(Name2)
mx=max(Name2)

print("Найменше значення температури=",mn,"*C")
print("Найбільше значення температури=",mx,"*С")
    
