import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=350)
window.config(padx=20, pady=20)

user_input = tkinter.Entry(width=10)
user_input.grid(column=3, row=1)

miles_to_km = tkinter.Label(text="0")
miles_to_km.grid(column=3, row=2)


def calculate():
    miles = user_input.get()
    km = float(miles) * 1.609344
    miles_to_km.config(text=km)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=4, row=1)
equals_to = tkinter.Label(text="equals to ")
equals_to.grid(column=1, row=2)

km_label = tkinter.Label(text="Km")
km_label.grid(column=4, row=2)
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=3, row=3)

window.mainloop()
