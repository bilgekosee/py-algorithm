# Klavyeden maaşı ve zam oranı girilen kişinin zamlı maaşını hesaplayan python kodunu yazınız.
maas = float(input("maasinizi girin: "))
zam = float(input("zamınızı float deeğrde girin ör:%25 ise 0.25 şeklinde :"))
son_maas = (maas*zam) + maas
print("yeni maasınız", son_maas)
