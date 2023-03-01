# Klavyeden girilen sayının pozitif mi negatif mi yoksa sıfır mı olduğunu bulan python kodunu yazınız.
sayi = int(input("bir sayi giriniz: "))
if (sayi < 0):
    print("bu sayi negatiftir")
elif (sayi > 0):
    print("bu sayi pozitiftir")
else:
    print("bu sayi sıfırdır")
