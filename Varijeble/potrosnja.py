# Ako je snaga mikrovalne pećnice 1.3 kWh, a cijena el. energije za 1 kWh je 0.95 kn, koliko kn mjesečno košta uporaba mikrovalne pećnice, ako se koristi 2 sata dnevno?
# Zbog jednostavnosti zaokružimo svaki mjesec na 30 dana.
# Ispišite trošak bez i s uračunatim PDV-om.


Snaga = 1.3 #kWh
Cijena = 0.95 #kn za 1 kWh
DnevnaPotrošnja = 2
BrojDanaUMjesecu = 30
PDV = 1.25


PotrošnjaPDV = (Snaga * Cijena * DnevnaPotrošnja * BrojDanaUMjesecu) * PDV

PotrošnjaBezPDV = Snaga * Cijena * DnevnaPotrošnja * BrojDanaUMjesecu

print ("Pozdrav, tvoja dnevna potrošnja bez PDV-a je", PotrošnjaBezPDV, "kn", ", a s PDV-om je", PotrošnjaPDV,"")









