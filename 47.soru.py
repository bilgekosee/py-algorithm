# Kullanıcının klavyeden kilo bilgisi alınarak kilo 50 ve altında ise zayıfsın, 50-80 arası fitsin, 80 ve üstü ise kilo almışsın şeklinde ekranda yazdıran python kodunu yazınız.
kilo = float(input("kilonuzu girin: "))
if (kilo < 50):
    print("zayıfsınız")
elif (50 < kilo < 80):
    print("fitsin")
else:
    print("kilo almışsın")
