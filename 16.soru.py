# Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen dikdörtgenin alan ve çevresini hesaplayan python kodunu yazınız.
kısa_kenar = int(input("dikdörtgenin kısa kenarını girin: "))
uzun_kenar = int(input("dikdörtgenin uzun kenarını girin: "))

alan = kısa_kenar*uzun_kenar
cevre = (kısa_kenar*2)+(uzun_kenar*2)

print("dikdörtgenin alanı ", alan)
print("dikdörtgenin çevresi ", cevre)
