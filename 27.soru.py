# Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan sayıların ortalamasını bulan python kodunu yazınız.
baslangic = int(input("baslangic sayisini gir: "))
bitis = int(input("bitis sayisini gir: "))
toplam = 0
sayac = 0
for x in range(baslangic, bitis+1):
    toplam += x
    sayac += 1
print("sayilariin ortalamasi :", (toplam/sayac))
