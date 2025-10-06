import tkinter as tk
import turtle as tr

window = tk.Tk()
window.title('My gui')
window.minsize(width = 400 , height = 400)

# label

my_label = tk.Label(text = 'center', font=('Arial',20,'normal'))
my_label.grid(row=0,column=0)
def change_label():
    parsed_input = my_input.get()
    my_label['text'] = parsed_input


# button

my_button = tk.Button(text = 'click me', command = change_label)
my_button.grid(row=1,column=1)

new_button = tk.Button(text = 'click me', command = change_label)
new_button.grid(row=0,column=2)

# input

my_input = tk.Entry()
my_input.grid(row=3,column=4)

# print(parsed_input)

window.mainloop()