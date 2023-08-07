#4.5 Kirjoita ohjelma, johon käyttäjä syöttää auton värin ja iän. Jos auto on nuorempi kuin 5 vuotta tai punainen, niin tulosta ”Ostetaan”, muulloin ”Ei osteta”.
avari = input("Mikä on auton väri?: ")
aian = input("Kuinka vanha auto on?: ")
aian = int(aian)
if avari == "punainen":
    print("Ostetaan")
elif aian == 5:
    print("Ostetaan")
else:
    print("Ei osteta")
