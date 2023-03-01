# 0 dan 100 e kadar olan çift sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
sayac = 0
top = 0
while sayac <= 100:
    sayac += 2
    top += sayac

print("0-100 arasındaki çift sayilarin toplami: ", top)
