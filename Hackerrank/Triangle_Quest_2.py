



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(''.join(map(str, (map(lambda x: i-abs(x-i),range(1,i*2))))))
    #metoda 2 aceasta functioneaza
    print(((10**i -1)//9)*((10**i -1)//9))
    #explicatie
    #cand i =1 ((10 **1-1)//9)*((10**1-1)//9) = (9//9)*(9//9)=1*1=1
    #cand i = 2 ((10 **2-1)//9)*((10**2-1)//9) =(99//9)*(99//9)=11*11=121
    #cand i = 3 ((10 **3-1)//9)*((10**3-1)//9)=(999//9)*(999//9)=111*111=12321
    #metoda 3
    print(*list(map(lambda x: i-abs(x-i),range(1,i*2))), sep='')
    #metoda 4
    print(sum(map(lambda n: 10**n, range(i)))**2)