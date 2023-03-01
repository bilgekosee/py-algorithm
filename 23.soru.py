# Klavyeden kısa kenar ve uzun kenar uzunluğu girilen dikdörtgenin alanını fonksiyon kullanarak hesaplayan python kodunu yazınız.
def dikdortgenAlan(genislik, yukseklik):
    alan = genislik * yukseklik
    print("Alan :", alan)
    return alan


gen = float(input("Genişlik :"))

yuk = float(input("Yükseklik : "))

dikdortgenAlan(gen, yuk)
