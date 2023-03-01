# Klavyeden girilen sayının asal sayı olup olmadığını bulan python kodunu yazınız.

sayac = 0
sayi = input('Bir Sayı Giriniz: ')
for i in range(2, int(sayi)):
    if (int(sayi) % i == 0):
        sayac += 1
        break
if (sayac != 0):
    print("Girilen Sayı Asal Değil")
else:
    print("Girilen Sayı Asal")
