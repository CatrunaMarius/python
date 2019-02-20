#cheacking a file extension

extensions = ['png', 'jpg', 'gif', 'svg']

fname = input().split('.')

if len(fname)>=2:
    fname_ext =fname[-1].lower()
    if fname_ext in extensions:
        print("yes")
    else:
        print("no")
else:
    print("the fname has no extension")