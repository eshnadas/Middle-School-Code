from robloxvibeusernames import RobloxName

password = open("rockyou.txt", "r", errors = "ignore")
otherPassword = password.readline()
incrementer = 0 
while otherPassword.strip() != "123456789":
    if RobloxName(otherPassword.strip()) == "123456789":
        print("omega cool awesome not sus hacker dude ")
        break 
    otherPassword = password.readline()
    print(otherPassword)
    incrementer = incrementer + 1 
print(" #omegaawesomehackerpro ")
print("ur password was " + str(incrementer) + "nd most popular")

 