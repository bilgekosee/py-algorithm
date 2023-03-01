#  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan çift sayıların toplamını bulan python kodunu yazınız.
bas = int(input("baslangic sayisini girin: "))
bitis = int(input("bitis sayisini girin: "))

toplam = 0
sayac = 0
for x in range(bas, bitis+1):
    if (x % 2 == 0):
        toplam += x
        sayac += 1
print("cift sayilarin toplami: ", toplam)
