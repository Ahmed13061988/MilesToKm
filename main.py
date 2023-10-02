import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=350)


def calculate():
    km = text.get() * 1.6
    return km


text = tkinter.Text(width=10, height=2)
text.grid(column=3, row=1)
label = tkinter.Label(text="Miles")
label.grid(column=4, row=1)
label2 = tkinter.Label(text="equals to ")
label2.grid(column=1, row=2)
label3 = tkinter.Label(text=0)
label3.grid(column=3, row=2)
label4 = tkinter.Label(text="Km")
label4.grid(column=4, row=2)
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=3, row=3)

window.mainloop()
