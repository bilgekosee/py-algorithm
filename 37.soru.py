#  Klavyeden aralarına virgül konularak yazılan tüm sayıları toplayan python kodunu yazınız.
numaralar = input("virgül ile sayıları girin: ")
print("girdiginiz sayilar: ", numaralar)

numaralarArr = numaralar.split(",")
toplam = 0
for n in numaralarArr:
    toplam += int(n)
print("girdiğniz sayilarin toplami: ", toplam)
