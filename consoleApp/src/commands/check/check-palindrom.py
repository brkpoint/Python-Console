

def dnb():    
    str = input("\n ENTER YOUR STRING HERE: ")
    strC = len(str) - 1
    index = strC
    for char in str:
        if char == str[index]:
            index = index - 1
        else:
            print(f"\n {str} word isnt a palindrom word!")
            return
        
    print("\n" + str + " is a palindrom word!")

dnb()