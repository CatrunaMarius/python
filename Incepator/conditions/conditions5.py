#Calculate mass, density or volume
result = None
#User chooses that he wants to calculate: mass(M) , density(d) or Volum(v)
flag=input("What to calculate? (m,d,v): ")

#if the mass is chosen, then you must ask for desity and volume. Calculate the mass by the formula m=d*v.
if flag=='m':
    #float() converts a string to real number
    d=float(input("Desity: "))
    v=float(input("Volume: "))
    result =d*v #density
#If  density is selected,than the mass and volume are requested. The formula d=m/v
if flag=='d':
    #float() converts a string to real number
    m=float(input("Massy: "))
    v=float(input("Volume: "))
    result =m/v #density

#if the volume is selected, the mass and desity are read. The volume is fund as v=m/d
elif flag =='v':
    m=float(input('Mass: '))
    d=float(input('Desity: '))
    result=m/d #volum

#regardless of the calculation branch, the result is written to the same 'result' variable.Formatted output with two decimal places
print("%.2f" % result)
