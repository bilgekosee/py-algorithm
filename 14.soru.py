# 1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
for x in range(1, 101):
    if (x % 15 == 0 and x % 3 == 0):
        print(x)
