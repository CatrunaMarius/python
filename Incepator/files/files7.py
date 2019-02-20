#Count the number of lines, words and letters in a text file

import sys
 
# argv - list of command-line arguments
# argv[0] - the script file name
# argv[1] - the first argument, it's the name of the file being processed
fname = sys.argv[1]
 
# Variables for counting strings, words and letters.
lines = 0
words = 0
letters = 0
 
# The open() function opens the file and returns an object,
# iteration over which allows to extract the lines of the file.
for line in open(fname):
    # A new line was received.
    # It is assigned to the variable 'line'.
    # The line counter should be increased by 1.
    lines += 1
 
    # Using len(), the number of characters in a string is determined
    # and added to the letter count.
    letters += len(line)
 
    # The code below counts the number of words in the current line.
 
    # A flag that signals the location outside the word.
    pos = 'out'
 
    # Bypassing line characters
    for letter in line:
        # If the current character is not a space, and
        # the flag is "outside the word", then a new word begins.
        if letter != ' ' and pos == 'out':
            # Thus, we must increase the word count by 1,
            words += 1
            # and change the flag to the value "inside the word".
            pos = 'in'
        # If the character is a space,
        elif letter == ' ':
            # then set the flag to "outside the word".
            pos = 'out'
 
# Display the number of lines, words and symbols on the screen.
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
