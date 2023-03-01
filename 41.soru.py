# 0 dan 100 e kadar olan tek sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.

sayac = 1
toplam = 0

while sayac <= 100:
    sayac += 2
    toplam += sayac

print("1-100 arasındaki tek sayılarin toplami: ", toplam)
