moja_lista = ["Pero", 20, True, "developer", "bla", False]
prazna_lista = [] #prazna lista

print(moja_lista)


# elementima liste pristupamo putem njihovih indeksa
# indeksi u listi kreću od 0

print(moja_lista[0])
# rint(prazna_lista[0]) greška jer pruistupamo indeksu koji ne postoji

# možemo zamijeniti vrijednost elementa na određenom indeksu
moja_lista[0] = "Perić"
print(moja_lista)


# Kreirajte mpvu listu sa brojevima od 1 do 5

lista_brojeva = [1,2,3,4,5]
print(lista_brojeva)

print(lista_brojeva[0])
print(lista_brojeva[4])
print(lista_brojeva[4])

# indeksi mogu biti i negativni - znaci da idemo u suprotnom smjeru
print(lista_brojeva[-1])


# kako prebrojati broj elemenata u listi?
print(len(lista_brojeva))
print(lista_brojeva[len(lista_brojeva)-1])


# ako želimo ispisati sve elemente u listi, potrebna nam je "for" petlja

osoba = ["Pero", "Perić", "Ilica 35", "Zagreb", "10000"]

"""
for element in osoba:   # umjesto element možemo dati bilo koji alias, "element" je samo primjer
    print(element)
print(osoba)
"""

for index, element in enumerate(osoba):
    print(index, element)
print(osoba)


# kreiraj listu od 10 brojeva i sve ispiši u istom retku
lista_brojeva_2 = [1,2,3,4,5,6,7,8,9,10]

for lista in lista_brojeva_2:
    print(lista, end= " ")