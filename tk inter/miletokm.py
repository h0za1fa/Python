import tkinter as tk

def miles_to_kms () :
    miles = int (kms_input.get())
    kms = round ( miles * 1.6 , 1)
    disp_result ['text'] = str (kms)

# setting up gui window
window = tk.Tk()
window.title('Mile to KM')
window.minsize(height=100,width=200)

# lables
unit_miles = tk.Label(text = 'Miles', font=('Arial',20,'normal'))
unit_miles.grid(row=0,column=3)

unit_kms=tk.Label(text = 'KMs', font=('Arial',20,'normal'))
unit_kms.grid(row=1,column=3)

dis_prompt = tk.Label(text = 'Is equal to', font=('Arial',20,'normal'))
dis_prompt.grid(row=1,column=0)

disp_result = tk.Label(text='0', font=('Arial',20,'normal'))
disp_result.grid(row=1,column=1)

calc_butt = tk.Button(text='calc', font=('Arial',20,'normal'), command=miles_to_kms)
calc_butt.grid(row=2,column=1)

kms_input = tk.Entry()
kms_input.grid(row=0,column=1)



window.mainloop()