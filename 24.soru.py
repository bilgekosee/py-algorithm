# Önceden belirlenen bir liste içerisinde bulunan sayılardan kaç tanesinin 5’in katı olduğunu bulan python kodunu yazınız.
sayilar = [18, 15, 22, 19, 85, 32, 65, 30, 95,
           10, 12, 20, 32, 55, 34, 28, 101, 5, 4, 32]
sayac = 0
for sayi in sayilar:
    if sayi % 5 == 0:
        print("{} sayısı 5'in katıdır.".format(sayi))
        sayac = sayac+1

print("5'in katı olan sayı adeti : "+str(sayac))
