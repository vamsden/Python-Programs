from tkinter import *

window = Tk()

topFrame = Frame(window)
topFrame.pack()

botFrame = Frame(window)
botFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Click1", fg="Red")
button1.pack()

button2 = Button(topFrame, text="Click2", fg="Blue")
button2.pack()

button3 = Button(botFrame, text="Click3", fg="Green")
button3.pack()

button4 = Button(botFrame, text="Click4", fg="Yellow")
button4.pack()

window.mainloop()
