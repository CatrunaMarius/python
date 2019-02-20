#Writing to a text file. Functia creaza si un fisier .txt
f=open("text.txt", 'w')

f.write("One ")
f.write("Two ")

f.writelines("Three ")

lst = ["Four ", "Five "]
f.writelines(lst)

f.close()

f = open("text.txt")
print(f.read())
f.close()
