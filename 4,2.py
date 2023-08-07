# 4.2 Kirjoita ohjelma, joka kysyy käyttäjän ikää. Täysi-ikäiselle tulostetaan ”Tervetuloa” ja alaikäiselle ”Poistukaa”.
luku1 = input("Mikä on sinun ikä?: ")
luku1 = int(luku1)
if luku1 >= 18:
    print("Tervetuloa")
else:
    print("Poistukaa")
