# Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
sayi = input('Bir Sayı Girin : ')
tekToplam = 0
ciftToplam = 0
for i in range(1, int(sayi)):
    if (i % 2 == 0):
        ciftToplam += i
    else:
        tekToplam += i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))
