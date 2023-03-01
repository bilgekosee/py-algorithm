# Python tkinter kütüphanesini kullanarak form penceresi ve Listbox (Liste kutusu) oluşturan kodunu yazınız.
from tkinter import *
from tkinter import messagebox

pencere = Tk()

pencere.title("https://github.com/bilgekosee")
pencere.geometry("400x300")

uygulama = Frame(pencere)
uygulama.grid()

Lb1 = Listbox(uygulama)
Lb1.insert(1, "londra")
Lb1.insert(2, "japonya")
Lb1.insert(3, "kanada")
Lb1.insert(4, "isveç")

Lb1.grid(padx=110, pady=10)

pencere.mainloop()
