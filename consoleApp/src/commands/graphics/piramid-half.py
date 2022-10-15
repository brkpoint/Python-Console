hPriamid = input("ENTER YOUR CHAR, NUMBER HERE: ")
hPriamidL = hPriamid.split(", ")

strP = ""
index = 1

print("\n half piramid here: \n")

for l in range(int(hPriamidL[1])):
    for p in range(index):
        strP = strP + hPriamidL[0]

    print(strP)
    
    strP = ""
    index = index + 1