broj = "5" #string
rijec = "dinamo" 
broj_int = int(broj) #integer
print(type(broj_int)) #funkcija type nam ispisuje kojeg je varijabla formata

broj_float = float(broj) #decimalni broj
print(broj_float, type(broj_float))

broj_2 = 10
broj_2_string = str(broj_2)
print(broj_2_string, type(broj_2_string))

print(bool(broj))
print(bool(rijec))
print(bool(broj_2))
print(bool("False"))
print(bool(""))
print(bool(" "))
print(bool("0"))

broj_2_binarni = bin(broj_2)
print(broj_2_binarni)
broj_2_heksadekadski = hex(broj_2)
print(broj_2_heksadekadski)
broj_2_okralni = oct(broj_2)
print(broj_2_okralni)

bla = "F"
bla_dekadski = int(bla, base = 16)