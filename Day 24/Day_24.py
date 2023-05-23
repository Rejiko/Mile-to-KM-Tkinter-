from tkinter import *

def convert_miles():
    miles = float(entry.get())
    km = round(miles * 1.609)
    calculatelabel = Label(text=f"{km}", font=("Arial", 13))
    calculatelabel.grid(column=1,row=1)

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=25)

mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

label1 = Label(text=" Miles", font=("Arial", 13))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Arial", 13))
label2.grid(column=0, row=1)

label3 = Label(text="Km", font=("Arial", 13))
label3.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_miles)
button.grid(column=1,row=2)

mainloop()