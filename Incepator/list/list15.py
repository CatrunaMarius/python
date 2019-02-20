#sorting words in a string by their length(ascending)
s = input()
w = s.split()
q = len(w)

for i in range(q-1):
    for j in range(q-1-i):
        if len(w[j])>len(w[j+1]):
            w[j], w[j+1]=w[j+1],w[j]

print(' '.join(w))