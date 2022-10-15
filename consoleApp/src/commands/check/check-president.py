im = input("ENTER YOUR <NAME>, <LASTNAME>, <AGE> HERE: ")
imL = im.split(', ')
wki = int(imL[2])

if wki >= 35:
    print("Hello, " + imL[0] + " " + imL[1] + ", you can be a president!")
if wki < 35:
    print("You cannot be a president becouse your age is below required 35!")