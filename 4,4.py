#4.4 Kirjoita ohjelma, johon käyttäjä syöttää iän. Määrittele itse ala- ja ylärajat. Jos ikä on rajojen sisällä, niin ohjelma tulostaa ”Rajojen sisällä”. 
#    Jos ikä on liian nuori, niin tulostaa ”Liian nuori” ja jos liian vanha, niin ”Liian vanha”.
luku1 = input("Ikä: ")
luku1 = int(luku1)
if luku1 > 60:
    print("Olet liian vanha.")
elif luku1 < 18:
    print("Olet liian nuori")
else:
    print("Pääset")
