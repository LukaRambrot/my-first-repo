# Napišite program koji od korisnika traži unos njegovog imena te ispisuje "Pozdrav, <ime>"

ime = input("Unesite ime: ")

print ("Pozdrav,", ime)



# Napišite program koji od korisnika traži unos sljedećih podataka:
# - ime
# - prezime
# - godina rođenja
# - država rođenja
# - status radnog odnosa
# - spol
# Sve unesene podatke je potrebno ispisati.


ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
godina_rođenja = int(input("Unesite godinu rođenja: "))
država_rođenja = input("Unesite državu rođenja: ")
status_radnog_odnosa = input("Unesite status radnog odnosa: ")
spol = input("Unesite spol: ")

print ("Bok", ime, prezime)
print ("Rođen si", godina_rođenja, "u", država_rođenja)
print ("Radni status ti je", status_radnog_odnosa)
print ("Spol je", spol)

