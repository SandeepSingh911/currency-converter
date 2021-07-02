from tkinter import *
from tkinter import ttk


converter = Tk()
converter.title("Currency Converter")
converter.geometry("600x400")

OPTIONS = {
    "Australian Dollar": 55.76,
    "Brazilian Real": 14.86,
    "British Pound": 102.66,
    "Chinese Yuan": 11.53,
    "Euro": 88.30,
    "HongKong Dollar": 9.62,
    "Indonesian Rupiah": 0.0051,
    "Japanese Yen": 0.67,
    "Pakistani Rupee": 0.47,
    "SriLankan Rupee": 0.37,
    "Swiss Franc": 80.70,
    "Us Dollar": 74.70,
}


def ok():
    price = amount.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer, None)
    converted = round(float(DICT)*float(price), 2)
    result.delete(1.0, END)
    result.insert(INSERT, converted)


appName = Label(converter, text="Currency Converter", font=(
    "arial", 25, "bold", "underline"), fg="dark red")
appName.place(x=150, y=10)

result = Text(converter, font=("arial", 20, "bold"), height=2, width=29,  bd=5)
result.place(x=89, y=60)

input = Label(converter, text="Value:",
              font=("arial", 10, "bold"), fg="red")
input.place(x=30, y=165)

amount = Entry(converter, font=("arial", 20))
amount.place(x=90, y=160)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter, variable1, *OPTIONS)
option.place(x=400, y=159, width=130, height=40)


button = Button(converter, text="Convert to Rupees", fg="green",
                font=("arial", 20), bg="powder blue", command=ok)
button.place(x=180, y=210, height=40, width=250)


converter.mainloop()
