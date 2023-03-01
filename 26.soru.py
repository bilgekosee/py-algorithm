#:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan tek sayıların ortalamasını bulan python kodunu yazınız.

sayi1 = int(input("baslangic sayiini gir: "))
sayi2 = int(input("bitis sayiini gir: "))
toplam = 0
sayac = 0

for x in range(sayi1, sayi2+1):
    if (x % 2 != 0):
        toplam += x
        sayac += 1
print("araliktaki tek sayilarin ortalamsi", (toplam/sayac))
