# IP adresa je adresa svakog računala na mreži koja se sastoji od četiri broja između 0 i 256. Primjer IP adrese: 192.168.0.184
# IP adresu iz primjera ispišite u binarnom, oktalnom i heksadekadskom obliku.
# SAVJET: za sada koristite zasebnu varijablu za svaki od četiri broja, odnosno dijela (okteta) IP adrese, ali ispišite ih u istom obliku kako je navedeno u primjeru (192.168.0.184).
# Ispis treba napraviti za sve oblike brojevnih sustava.


IP_adresa_1 = 192
IP_adresa_2 = 168
IP_adresa_3 = 0
IP_adresa_4 = 184

print("Binarni oblik IP adrese je: ", end= "")
print(bin(IP_adresa_1),bin(IP_adresa_2),bin(IP_adresa_3),bin(IP_adresa_4), sep = ".")

print("Okralni oblik IP adrese je: ", end= "")
print(oct(IP_adresa_1),oct(IP_adresa_2),oct(IP_adresa_3),oct(IP_adresa_4), sep = ".")

print("Heksadekadski oblik IP adrese je: ", end= "")
print(hex(IP_adresa_1),hex(IP_adresa_2),hex(IP_adresa_3),hex(IP_adresa_4), sep = ".")
