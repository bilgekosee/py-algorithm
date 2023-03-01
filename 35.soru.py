# Bir otoparkın ücret tarifesi aşağıdaki gibidir:

# 1 saate kadar: 10 TL
# 1-5 saat arası: Saat başı 8 TL
# 5 saatten fazla: Saat başı 6 TL
# Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız.

sure = float(input("otoparkta bulunduğunuz saatin siresini yazın: "))
if (sure <= 1):
    ucret = 10
    print("odeyeceğiniz ucret: ", ucret)
if (1 < sure < 5):
    ucret = sure*8
    print("odeyeceginiz ucret : ", ucret)
else:
    ucret = sure*6
    print("odeyeceginiz ucret : ", ucret)
