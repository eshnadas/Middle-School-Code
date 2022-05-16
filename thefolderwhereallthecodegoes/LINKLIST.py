class Node:
    def __init__(self):
        self.data = ""
        self.next = None 
class LINKLIST:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.numNode = 0
    
    def addHead(self, data):
        #add to link list
        firstNODE = Node()
        firstNODE.data = data 
        if self.numNode > 0:
            firstNODE.next = self.head
        else:
            self.tail = firstNODE
        self.head = firstNODE
        self.numNode = self.numNode + 1 

    def printListtt(self):
        iterNODE = self.head 
        while iterNODE is not None:
            print(iterNODE.data)
            iterNODE = iterNODE.next   

    def addTAIl(self, data):
        firstNODE= Node()
        firstNODE.data = data
        if self.numNode > 0:
            self.tail.next = firstNODE
        else:
            self.head = firstNODE
        self.tail = firstNODE
        self.numNode = self.numNode + 1 

    def insertSomethingFancy(self, data, position):
        if position == 0:
                addHead()
                return
        if position == self.numNode:
            addTAIl()
            return
        firstNODE = Node()
        firstNODE.data = data
        iterNODE = self.findNODEATposiTion(position) 
        firstNODE.next = iterNODE.next
        iterNODE.next = firstNODE
 
    def findNODEATposiTion(self, position): 
        Counter = 0 
        iterNODE = self.head
        while iterNODE is not None:
            # print(iterNODE.data)
              
            if Counter == position:
                return iterNODE
                break
            Counter = Counter + 1
            iterNODE = iterNODE.next

    def addHEADSSSS(self, datas):
        for node in datas: 
            self.addHead(node)
    def addTAILSSSS(self, datas):
        for node in datas:
            self.addTAIl(node)

    def somethingFANCIER(self, datas, position):
        for node in datas:
            self.insertSomethingFancy(node, position)

    def swapppeFORWARD(self,position):
        iterNODE = self.findNODEATposiTion(position+1)
        temp = iterNODE.data 
        iterNODE.data = iterNODE.next.data
        iterNODE.next.data = temp 
    
    def swapppeBACKWARDS(self, position):
        iterNODE = findNODEATposiTion(position)
        temp = iterNODE.data 
        iterNODE.data = self.findNODEATposiTion(position-1)
        self.findNODEATposiTion(position-1).data = temp 

    def positionCALLER(self,data):
        iterNODE = self.head
        counter = 0 
        while iterNODE is not none:
            if data == iterNode.data:
                return counter
            else:
                counter = counter + 1 

    def returnList(self):
        idksmh = ""
        iterNODE = self.head 
        
        while iterNODE is not None:
            idksmh += " " 
            idksmh += iterNODE.data[0]
            idksmh += " "
            idksmh += iterNODE.data[1]
            iterNODE = iterNODE.next
        return idksmh

    def __str__(self):
        return self.returnList()
    
    def delete(self,position):
        if position > 0 and position < self.numNode:
            node = self.findNODEATposiTion(position-1)
            node.next = self.findNODEATposiTion(position+1) #or node.next.next
        elif position == 0:
            head = self.head
            self.head = head.next 
            del head 
        # elif position = self.numNode:
        #     tail = self.tail
        #     self.tail = tail.before
        


        #remove the node and then check other stuff
        
    


        


        
 
# linkedlist = LINKLIST()
# # linkedlist.addHEADSSSS(["aojefiae", "AssertionError", "param datas", "ladelaalalaegjfoijareoigdj"])
# # linkedlist.addTAILSSSS(["aeghij", "Failure", "FALSE", "it'sSoHardToThinkOfWordsOffTheBat"])
# # linkedlist.somethingFANCIER("oplaeirziagrjoiejgiohgjridjvmciomiocmlaiejwofjici",3)
# linkedlist.swapppeFORWARD(2)
# # linkedlist.addTAIl("oiaioaegragjioejogiergoeijoINk")
# # linkedlist.addTAIl("hola-bonjour-aloha")
# # linkedlist.addTAIl("uhhhhhh_idk what to say")
# # linkedlist.printListtt()
# # linkedlist.addHead("feijOEFWEIjjiIJijfeIFEDJORNEDSVHBHAJIKNijvkcmjhgut987tyghbfjdncxkmljish")
# # linkedlist.addHead("hi.")
# # linkedlist.addHead("lalallalalalallalalalalaalalalallalalala")
# # linkedlist.printListtt()
# # linkedlist.addHead("hi")
# # linkedlist.addTAIl("bye")
# # linkedlist.insertSomethingFancy("hibye", 1)
# linkedlist.printListtt()
