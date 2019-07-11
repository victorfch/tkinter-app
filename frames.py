import tkinter

window = tkinter.Tk()
#frames
top_frame = tkinter.Frame(window)
bottom_frame = tkinter.Frame(window)

#labels
header_label = tkinter.Label(top_frame, text = "Demo")
footer_label = tkinter.Label(bottom_frame, text = "End of app")

#packagging
top_frame.pack()
bottom_frame.pack(side = tkinter.BOTTOM)
header_label.pack()
footer_label.pack()
window.mainloop()