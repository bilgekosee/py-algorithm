# Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan sayıların toplamını bulan python kodunu yazınız.
bas = int(input("baslangic sayisini gir: "))
bitis = int(input("bitis sayisini gir: "))
toplam = 0
for x in range(bas, bitis+1):
    toplam += x
print("aradaki sayilarin toplami ", toplam)
