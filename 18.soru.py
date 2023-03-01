#  Klavyeden girilen iki sayı arasındaki sayıları toplayan python kodunu yazınız.
toplam = 0
sayi1 = int(input('1. Sayıyı Giriniz: '))
sayi2 = int(input('2. Sayıyı Giriniz: '))
for i in range(sayi1+1, sayi2):  # başlangıç ve bitiş sayılarını dahil etmez !!!
    toplam += i
print(sayi1, " ile ", sayi2, "arasındaki sayıların toplamı :", toplam)
