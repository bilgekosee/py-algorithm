# Klavyeden başlangıç değeri, bitiş değeri ve artış miktarı girilen sayıları alt alta yazdıran python kodunu yazınız.
baslangic = int(input("baslangic deger gir: "))
bitis = int(input("bitis degeri gir: "))
artis_mikatari = int(input("artış miktarını gir: "))

for x in range(baslangic, bitis, artis_mikatari):
    print(x)
