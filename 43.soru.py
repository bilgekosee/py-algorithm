# Klavyeden girilen sayıya kadar olan tek sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
sayi = int(input("sayi gir: "))
toplam = 0
sayac = 1
while sayac <= sayi:
    toplam += sayac
    sayac += 2

print("girilen sayiya kadar olan tek sayıların toplamı: ", toplam)
