a = input()
b = ""
s = []
for i in a:
    if i != " ":
        b += i
    else:
        s.append(b)
        b = ""
s.append(b)
print(min(s, key=len))
print(max(s, key=len))
