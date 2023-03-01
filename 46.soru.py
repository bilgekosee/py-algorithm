# 0 ile 100 arasında 10 tane rastgele tam sayı üreten ve bu sayılardan en büyüğü ile en küçüğünü bulan ve ekranda gösteren python kodunu yazınız.

import random
sayilar = []
for i in range(0, 10):
    rast = random.randint(0, 100)
    sayilar.append(rast)
    print(rast)

enkucuk = sayilar[0]
enbuyuk = sayilar[0]

for i in range(0, 10):
    if enkucuk > sayilar[i]:
        enkucuk = sayilar[i]
    if enbuyuk < sayilar[i]:
        enbuyuk = sayilar[i]

print("en buyuk deger: ", enbuyuk)
print("en kucuk deger: ", enkucuk)
