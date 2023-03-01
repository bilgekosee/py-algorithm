#  Klavyeden aralarına virgül konularak yazılan tüm sayıların ortalamasını hesaplayan python kodunu yazınız.
numaralar = input("Virgül ile sayıları giriniz.: ")

print("Girdiğiniz Sayılar: {0}".format(numaralar))

numaralarArr = numaralar.split(",")
toplam = 0
for n in numaralarArr:
    toplam = toplam + int(n)

print("GİRDİĞİNİZ SAYILARIN ORTALMASI:{0:.2f} ".format(
    toplam / len(numaralarArr)))
