class Node:
    def __init__(self):
        self.data = ""
        self.next = None 
        self.prev = None

firstNODE = Node()
secondNODE = Node()
thirdNODE = Node()

firstNODE.data = "ESHAN"
secondNODE.data = "mR_WiTTMaYEr"
thirdNODE.data = "ehioru"
firstNODE.next = secondNODE
secondNODE.next = thirdNODE
secondNODE.prev = firstNODE
thirdNODE.prev = secondNODE

ITERNODE = firstNODE 
COUNTER = 0
while ITERNODE is not None:
    if ITERNODE.data == "mR_WiTTMaYEr":
        print(COUNTER)
        break
    else: 
        ITERNODE = ITERNODE.next
    COUNTER = COUNTER + 1        