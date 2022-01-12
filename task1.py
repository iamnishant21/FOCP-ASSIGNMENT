print("Stop! Who would cross the Bridge of Death")
print("Must answer me these questions three, 'ere the other side he see.")

name = input("What is your name?")
if name.upper()=="ARTHUR":
    print("My liege! You may pass!")
else:
    seek = input("what is your quest?")
    if seek.upper().find("GRAIL")==-1:
        print("Only those who seek the Grail may.")
    else:
        colour= input("what is favourite colour?")
        if colour.upper().find(name[0].upper())==0:
            print("You may pass.")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")