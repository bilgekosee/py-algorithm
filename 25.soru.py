# Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan çift sayıların ortalamasını bulan python kodunu yazınız.

toplam = 0
sayac = 0
baslangic = int(input("Başlangıç Sayısı :"))
bitis = int(input("Bitiş Sayısı :"))
for sayi in range(baslangic, bitis+1):
    if (sayi % 2 == 0):
        toplam = toplam+sayi
        sayac = sayac+1
print('Ortalama', (toplam/sayac))
