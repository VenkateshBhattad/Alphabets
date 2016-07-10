from Tkinter import *
import tkFont
import pyttsx
engine = pyttsx.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
def onKeyPress(event):
    label.configure(text=event.char)
root = Tk()
root.wm_title("Alphabet")
customFont = tkFont.Font(family="Helvetica", size=100)
var = StringVar()
label = Label( root, width=10, height=5, font=customFont, bg="Green", fg="Red" )
root.bind("<KeyPress>", onKeyPress)
label.pack()
root.mainloop()
