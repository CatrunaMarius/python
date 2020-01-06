

#Vi se oferă un șir care constă numai din cifrele 0-9, virgule, și puncte.

#Sarcina dvs. este să completați regex_pattern definit mai jos, care va fi utilizat pentru a re.split () toate, și. simboluri în s.

#Este garantat că fiecare virgulă și fiecare punct din s sunt precedate și urmate de o cifră.

#Sample Input 0

#100,000,000.000
#Sample Output 0

#100
#000
#000
#000

regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#metoda 2
import re
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')

#metoda 3
list = [1,2,3]
print(*list, sep=",")