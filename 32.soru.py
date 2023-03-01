# Python tkinter kütüphanesini kullanarak form penceresi ve Entry (metin kutusu) oluşturan kodunu yazınız.
from tkinter import *
from tkinter import messagebox
pencere = Tk()

pencere.title("https://github.com/bilgekosee")
pencere.geometry("320x175")

# grid from çizdirme
uygulama = Frame(pencere)
uygulama.grid()

L1 = Label(uygulama, text="metin girin ")
L1.grid(padx=110, pady=10)

E1 = Entry(uygulama, bd=2)
E1.grid(padx=100, pady=3)

# formu çiz
pencere.mainloop()
