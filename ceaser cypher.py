from ceaserart import logo

def ceaser(msg,letters,shift,choice):
    encrypted=''
    if choice == 'd':
            shift = -shift
    for alph in msg :
        ind = letters . index (alph)
        ind = (ind+shift)%len(letters) 
        encrypted += letters [ind]
    return encrypted

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo
choice=input('encode (e) or decode (d) \n')
msg=input('Enter meseasge \n')
shift=int(input('Enter shift \n'))
print(ceaser(msg,letters,shift,choice))

# gttgnjx gttgnjxj
