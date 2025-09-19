from ceaserart import logo

def ceaser ( msg , letters , shift , choice ) :
    msg=msg
    encrypted = ''
    if choice == 'd':
        shift = - shift
    for alph in msg :
        if alph not in letters:
            encrypted+=alph
        else:    
            ind = letters . index (alph)
            ind = (ind + shift) % len (letters) 
            encrypted += letters [ind]
    return encrypted


letters=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

sent=''
word=[]
conti='Y'

logo
while conti=='Y':
    choice=input('encode (e) or decode (d) \n')
    msg=input('Enter meseasge \n').split()
    shift=int(input('Enter shift \n'))
    for words in msg:
        word.append(ceaser(words,letters,shift,choice))
        
    sent=' '.join(word)
    print(sent)
    word=[]
    conti=input('If you want to continue press Y: ').upper()
    print("-----------------------------------------")