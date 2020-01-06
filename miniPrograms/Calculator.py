import math
print("====calculator simplu====")




while True:
    
  
    n1 =input("a")
   
    
    while n1 != "c" :
      try:
        val = float(n1)
        
        
        break
      except ValueError:
        print("introduce un numara")
        n1 = input("b")
    if  n1 == "c":
        break    
     
     
        
    i = input("c")
    if  i == "c":
       break   
    
    if i == "+":
        n2 = input()
        if n2 == "c":
            break
        rz =float(n1)+float(n2)
        print(rz)
    elif i == "log10":
        log10 =math.log10(float(n1))
        print(log10)
    elif i == "log2":
        log2 =math.log2(float(n1))
        print(log2)
    elif i == "log1p":
        log1p =math.log1p(float(n1))
        print(log1p)
    elif i == "log":
        n2 = input("baza: ")
        if n2 == "c":
            break
        log = math.log(float(n1),float(n2))
        print(log)
        
    elif i == "sin":
        print(math.sin(float(n1)))
    elif i == "cos":
        cos =math.cos(float(n1))
        print(cos)
    elif i == "l10+":
        n2 = input()
        if n2 == "c":
            break
        print(math.log10(float(n1))+math.log10(float(n2)))
    elif i == "l10-":
        n2 = input()
        if n2 == "c":
            break
        print(math.log10(float(n1))-math.log10(float(n2)))
    elif i == "l10*":
        n2 = input()
        if n2 == "c":
            break
        print(math.log10(float(n1))*math.log10(float(n2)))
    elif i == "l10/":
        n2 = input()
        if n2 == "c":
            break
        print(math.log10(float(n1))/math.log10(float(n2)))
    elif i == "rad":
        print(math.sqrt(float(n1)))
    elif i == "-":
        n2=input()
        if n2 == "c":
            break
        print(float(n1)-float(n2))
    elif i == "/":
        n2 = input()
        if n2 == "c":
            break
        while n2 ==0 :
          n2=float(input("divizarea cu zero nu este posibila incercati un alt numar: "))
          
        print(float(n1)/float(n2))
    elif i == "*":
        n2 = input()
        if n2 == "c":
            break
        print(float(n1)*float(n2))
    elif i == "**":
        n2 =input()
        if n2 == "c":
            break
        re = pow(float(n1),float(n2))
        print(re)
    
    
    else:
        print("eroare: ati introdus altceva decat unul din: +  - * / ** cos sin log log10 log2 log1p ")
