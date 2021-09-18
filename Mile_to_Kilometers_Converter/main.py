from tkinter import *


def convert():
    mile = entry.get()
    km = float(mile) * 1.609
    result.config(text=f"{round(km, 2)}")


# window screen
screen = Tk()
screen.title("Miles to Kilometers Converter")
screen.config(padx=20, pady=20)

# Entry
entry = Entry(width=20)
entry.grid(column=1, row=0)
entry.insert(END, string= "Enter a number")

# Label
label_1 = Label(text="is equal to", font=("Courier", 15, "bold"))
label_1.grid(column=0, row=1)

label_1 = Label(text="Miles", font=("Courier", 15, "bold"))
label_1.grid(column=2, row=0)

label_1 = Label(text="Km", font=("Courier", 15, "bold"))
label_1.grid(column=2, row=1)

result = Label(text="0", font=("Courier", 20, "bold"))
result.grid(column=1, row=1)

# Button
button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)

screen.mainloop()
