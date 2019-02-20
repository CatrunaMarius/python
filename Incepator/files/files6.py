#replace tab symbols with four spaces
tab_file = open("tab.txt")
tab_text = tab_file.read()
tab_file.close()
print(repr(tab_text))

list_text = tab_text.split('\t')
space_text = '    '.join(list_text)
print(repr(space_text))

space_file = open("space.txt", 'w')
space_file.write(space_text)
space_file.close()
