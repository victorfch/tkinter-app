import tkinter

window = tkinter.Tk()
message = "Hello World"
label_hello = tkinter.Label(window, text = message)
label_hello.pack()
window.mainloop()