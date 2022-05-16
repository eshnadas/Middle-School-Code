def RobloxName(name):
    NEWROBLOXSUPERCOOLNAME = ""
    for i in name:
        if i == "e":
            NEWROBLOXSUPERCOOLNAME = NEWROBLOXSUPERCOOLNAME + "3"
        elif i == "o":
            NEWROBLOXSUPERCOOLNAME = NEWROBLOXSUPERCOOLNAME + "0"
        elif i == "l":
            NEWROBLOXSUPERCOOLNAME = NEWROBLOXSUPERCOOLNAME + "1"  
        elif i == "a":
            NEWROBLOXSUPERCOOLNAME = NEWROBLOXSUPERCOOLNAME + "@"
        elif i == "s":
            NEWROBLOXSUPERCOOLNAME = NEWROBLOXSUPERCOOLNAME + "$"
        else:
            NEWROBLOXSUPERCOOLNAME = NEWROBLOXSUPERCOOLNAME + i
    return NEWROBLOXSUPERCOOLNAME
print(RobloxName("midnightgalaxymoon3"))       
        
    