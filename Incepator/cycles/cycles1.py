#output of the ASCII caracte table
#caractrele din tabelul ASCII de la 32 la 128 sunt afisate cu codul acesta
for i in range(32, 128):
    print(chr(i), end=' ')
    if(i-1)%10==0:
        print()
print()