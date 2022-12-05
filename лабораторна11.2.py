import json
x=", "

disk1={"Name": "CD-RW", "Price": "200HRN", "Size": "7GB"}       
disk2={"Name": "CD-R", "Price": "150HRN", "Size": "5GB"}
disk3={"Name": "DWD-R", "Price": "250HRN", "Size": "6GB"}

dsk1=(json.dumps(disk1))
dsk2=(json.dumps(disk2))
dsk3=(json.dumps(disk3))
data=dsk1,dsk2,dsk3 

c=(sorted(data))
print(x.join(c))

    

