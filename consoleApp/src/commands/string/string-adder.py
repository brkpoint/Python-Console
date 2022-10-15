strInt = input("ENTER YOUR STRING, NUMBER HERE: ")
strIntL = strInt.split(", ")

strFinalWord = ""

for intS in range(int(strIntL[1])):
    strFinalWord = strFinalWord + strIntL[0]

print(strFinalWord)