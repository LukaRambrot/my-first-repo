# Zadatak na stranici https://usbrandcolors.com/google-colors/ imate boje Google logotipa.
# Pomoću odgovarajućih naredbi za konverziju pokušajte pretvoriti RGB zapise iz HEX u dekadski.
# Primjer: 
# Naziv boje:
#   
# 
#   Blue = #4285F4
#   Red = #DB4437
#   Yellow = #F4B400
#   Green = #0F9D58



Blue1 = "42"
Blue2 = "85"
Blue3 = "F4"

Red1 = "DB"
Red2 = "44"
Red3 = "37"

Yellow1 = "F4" 
Yellow2 = "B4"
Yellow3 = "00"

Green1 = "0F"
Green2 = "9D"
Green3 = "58"


print("Blue - dekadski oblik: ", end= "")
print(int(Blue1,16),int(Blue2,16),int(Blue3,16))

print("Red - dekadski oblik: ", end= "")
print(int(Red1,16),int(Red2,16),int(Red3,16))

print("Yellow - dekadski oblik: ", end= "")
print(int(Yellow1,16),int(Yellow2,16),int(Yellow3,16))

print("Green - dekadski oblik: ", end= "")
print(int(Green1,16),int(Green2, 16),int(Green3,16))
