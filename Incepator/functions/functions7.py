# In a string, change the word sequence to reverse
def reverse_words(s):
    s =s.split()
    s.reverse()
    return ' '.join(s)

print(reverse_words(input()))
