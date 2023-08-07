#4.3 Kirjoita ohjelma, joka kysyy pin-koodia. Pin-koodin arvo on 1234. Käyttäjälle tulostetaan, että onko vastaus oikein.
luku1 = input("Pin-koodi: ")
luku1 = int(luku1)
if luku1 == 1234:
    print("Oikein")
else:
    print("Väärin")
