#Beautiful digits from Unicode
digits = {0:  9471, 1:10102, 2: 10103, 3: 10104,
          4: 10105, 5:10106, 6: 10107, 7: 10108,
          8: 10109, 9:10110, 10: 10111}

n = input("Input: ")

new_n= ""

for i in n:
    i = int(i)
    i = chr(digits[i])
    new_n = new_n + i

print("Output: %s" % new_n)
