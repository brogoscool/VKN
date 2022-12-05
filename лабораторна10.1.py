storytxt = open(r"C:\\Program Files\\Git\\repos\\VKN\story.txt")
data = storytxt.read()
words = data.split()
word=data.split(".")
unique=set(words)



print("Кількість унікальних слів:", len(unique))
print("Кількість слів в файлі:", len(words))
print("Кількість речень в файлі:", len(word))