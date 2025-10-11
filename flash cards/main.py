import tkinter as tk
import pandas as pd
import random as rn
import time as tm

BACKGROUND_COLOR = "#B1DDC6"
en_word = ''
words_to_know=[]

# <---------------------------------DISP WORDS--------------------------------->

def flip_card(en_word):
    card.itemconfig(disp_card, image=card_back )
    card.itemconfig(word_disp, text = en_word, fill = 'white')

def select_word(status):
    global timer_delay
    global en_word
    global words_to_know
    window.after_cancel(timer_delay)
    fr_word = ''
    en_word = ''
    card.itemconfig(disp_card, image=card_front )
    data = pd.read_csv('flash cards/data/french_words.csv')
    data_dict = data.to_dict(orient="records")
    # print(data_dict)
    ind_val = rn.randint(0,len(data_dict)-1)
    word_set = data_dict[ind_val]
    fr_word, en_word = word_set.values()
    card.itemconfig(word_disp, text = fr_word, fill = BACKGROUND_COLOR)
    timer_delay = window.after(3000, flip_card, en_word)
    # print(word_set)
    
    words_to_know_dict = {fre: eng for (fre,eng) in word_set.items() if status == True}
    if words_to_know_dict != {}:
        words_to_know.append(words_to_know_dict)
    data_dict.remove(word_set)
# <---------------------------------UI setup--------------------------------->

window = tk.Tk()
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
timer_delay = window.after(3000, flip_card, en_word)

# canvas card setup

card_front = tk.PhotoImage(file ='flash cards/images/card_front.png')
card_back = tk.PhotoImage(file ='flash cards/images/card_back.png')
card = tk.Canvas(width=800,height=524, background=BACKGROUND_COLOR, highlightthickness=0)
disp_card = card.create_image(400, 262 , image=card_front )
card.grid(column=1,row=1,columnspan=2)
word_disp = card.create_text(400,262,text='',font=('Ariel', 40, 'bold'))
select_word(False)

# right and wrong button

right_img=tk.PhotoImage(file='flash cards/images/right.png')
wrong_img=tk.PhotoImage(file='flash cards/images/wrong.png')

right_butt = tk.Button(image=right_img,height=100,width=100, background=BACKGROUND_COLOR,relief='flat',command=lambda: select_word(False))
wrong_butt = tk.Button(image=wrong_img,height=100,width=100, background=BACKGROUND_COLOR,relief='flat',command=lambda: select_word(True))

right_butt.grid(row=2, column=1)
wrong_butt.grid(row=2, column=2)



window.mainloop()

# print(words_to_know)
df = pd.DataFrame(words_to_know)
df.to_csv('flash cards/data/words_to_learn.csv')