from Tkinter import *
import tkFont
import pyttsx
def onKeyPress(event):
    label.configure(text=event.char)
    talkTheChar(event.char)
    
def talkTheChar(str):
    engine = pyttsx.init()
    engine.setProperty('rate', 100)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(str)
    engine.runAndWait()
root = Tk()
root.wm_title("Alphabet")
customFont = tkFont.Font(family="Helvetica", size=100)
var = StringVar()
label = Label( root, width=10, height=5, font=customFont, text="A", bg="Green", fg="Red" )
root.bind("<KeyPress>", onKeyPress)
label.pack()
root.mainloop()
