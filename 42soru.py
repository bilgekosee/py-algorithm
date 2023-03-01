# Klavyeden girilen sayıya kadar olan sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
sayi = int(input("bir sayi gir: "))
toplam = 0
sayac = 0
while sayac <= sayi:
    toplam += sayac
    sayac += 1

print("sayilarin toplami: ", toplam)
