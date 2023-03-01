# Klavyeden girilen sayıya kadar olan çift sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
sayi = int(input("bir sayi girin: "))
top = 0
sayac = 0
while sayac <= sayi:
    top += sayac
    sayac += 2
print("girilen sayiya kadar olan çift sayilarin toplami: ", top)
