#  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan tek sayıların toplamını bulan python kodunu yazınız.
bas = int(input("baslangic sayisini gir: "))
bit = int(input("bitis sayisini gir: "))
toplam = 0
sayac = 0
for x in range(bas, bit+1):
    if (x % 2 != 0):
        toplam += x
        sayac += 1
print("tek sayilarin toplami ", toplam)
