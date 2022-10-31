

ime = "Pero"
godine = 20
punoljetan = True
zanimanje = "Developer"


print(ime, "ima", godine, "godina.", end= " ")
print("Njegovo zanimanje je", zanimanje, end= ".")
print("To je to za danas.")


print("{} ima {} godina. Njegovo zanimanje je {}. To je to za danas.".format(ime,godine,zanimanje) )




# f-string

print(f"{ime} ima {godine} godina. Njegovo zanimanje je {zanimanje}. To je to za danas")