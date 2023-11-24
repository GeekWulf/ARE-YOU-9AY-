import tkinter as tk
from PIL import ImageTk, Image
import time 
import random

window = tk.Tk()
window.geometry("1000x500")

xpos = 465
ypos = 120


def Enter():
    global xpos, ypos
    xpos = random.randrange(10, 910, 1)
    ypos = random.randrange(5, 430, 1)
    i = 1
    while i == 1:

        Label.pack()
        Label.configure(font = Font_label)
        Yes_Button.place(x = 455, y = 200)
        Yes_Button.configure(font = Font_Yes_button)
        No_Button.place(x = xpos, y = ypos)
        No_Button.configure(font = Font_No_button)  
        print(xpos, ypos)
        i = not i

def Lose():
    print("You're gay")
    #Creating_Img()

'''
def Creating_Img():
    pass
'''
    
Font_label = ("Comic Sans MS", 20, "bold")
Font_Yes_button = ("Minion Pro Cond", 20, "bold")
Font_No_button = ("Minion Pro Cond", 20, "bold")

Label = tk.Label(master = window, text = "ARE YOU GAY?")
Yes_Button = tk.Button(master = window, text = 'YES!', command = Lose)
No_Button = tk.Button(master = window, text = 'NO!', command = Enter)

Label.pack()
Label.configure(font = Font_label)
Yes_Button.place(x = 455, y = 200)
Yes_Button.configure(font = Font_Yes_button)
No_Button.place(x = xpos, y = ypos)
No_Button.configure(font = Font_No_button)
'''
img1 = Image.open('png imgs.png')
new_img1 = img1.resize((1000, 500))
new_img1.save('gay mans kissing edited.gif')
bg1 = ImageTk.PhotoImage(new_img1)
canva = tk.Label(window, image = bg1)
canva.place(x = 0, y = 0)
'''

window.mainloop()