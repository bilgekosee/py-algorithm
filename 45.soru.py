# Klavyeden girilen bir metni harflerine ayıran python programını while döngüsü ile yazdıran kodunu yazınız.
metin = input("bir metin gir: ")
sayac = 0

while sayac < len(metin):
    print(metin[sayac])
    sayac += 1
