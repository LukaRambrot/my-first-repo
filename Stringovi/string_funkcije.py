ime = "Pero"
zanimanje = "developer"


# ispisuje string sa SVIM malim slovima
print(ime.lower())

# ispisuje string sa SVIM velikim slovima
print(ime.upper())

# ispisuje veliko početno slovo
print (zanimanje.capitalize())

# ispisuje koliko string ima znakova
print(len(ime))

# string je niz znakova.
# svakom znaku možemo pristupiti putem njegovog indeksa.
# Indek je pozicija slova u stringu i bitno je zapamtiti da indeksi kreću od 0.
print(ime[0])
print(ime[1])
print(ime[2])
print(ime[3])

# Ispisujemo duljinu stringa u varijabli zanimanje te slova na prvoj, trećoj i petoj poziciji.
print(len(zanimanje))
print(zanimanje[0], zanimanje[2], zanimanje[4])



ime_2 = "Pepo"

# želimo prebrojati koliko se puta određeno slovo pojavljuje u stringu
print(ime.count("e"))
print(zanimanje.count("e"))
print(ime_2.count("p"))
print(ime_2.lower().count("p"))


# želimo naći gdje nam se u našem stringu zanimanje pojavljuje slovo "e"

print (zanimanje.find("e")) #vraća 1 - indeks prvog pojavljivanja slova "e" u riječi "developer"
