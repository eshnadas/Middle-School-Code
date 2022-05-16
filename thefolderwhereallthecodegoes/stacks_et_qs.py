class stack:

    def __init__(self):
        self.stacklist = []
        
    def push(self, addything):
        self.stacklist.append(addything)

    def pop(self):
        poppee = self.stacklist[-1]
        del self.stacklist[-1] 
        return poppee

    def peek(self):
        peekee = self.stacklist[-1]
        return peekee

    def size(self):
        size = len(self.stacklist)
        return size
    
    def isempty(self):
        if len(self.stacklist) == 0:
            return True
        else:
            return False


def palindrome(word):
    stacklist = stack()
    for i in word:
        stacklist.push(i)
    for i in range(len(word)):
        peeked = stacklist.peek()
        stacklist.pop()
        if word[i] != peeked:
            print("you are so stupid do you even know what a Palindrome is ? That's what i thought")
            return False
    print("nice. you actually have a brain!")    
    return True

def parentTHESIS(equation):
# ((1+2)/6)
#start w open- end w close
# same amt of opens and closed
#finish a pair before move on 
# (
# )
# )
# (
    stacklist = stack()
    for i in equation:
        if i != "(" and i != ")":
            continue 
        else:
            if i == "(":
                stacklist.push(i)
            elif i == ")" and stacklist.size() == 0:
             
                return False
            elif stacklist.size() > 0:
                stacklist.pop()    
    if stacklist.size() == 0:
        print("yas queeeeeeeeeeen pop awfffffff")       
        return True
    if stacklist.size() != 0:
        print("ur so stupid u dont even know how many parenthesis u need oh my god u imbecile")   
        return False   
parentTHESIS("())")

    
class Qew:

    def __init__(self):
        self.queuelist = []

    def enqueue(self,addything):
        self.queuelist.insert(0, addything)

    def dequeue(self):
        deletionism = self.queuelist[-1]
        del self.queuelist[-1]
        return deletionism

    def front(self):
        frontism = self.queuelist[-1]
        return frontism

    def isempty(self):
        if len(self.queuelist) == 0:
            return True
        else:
            return False


# queuelist = Qew()
# queuelist.enqueue(1)
# queuelist.enqueue(123)
# queuelist.enqueue(9)
# queuelist.dequeue()
# queuelist.enqueue(2)
# print(queuelist.front())
# queuelist.dequeue()
# print(queuelist.front())
# queuelist.enqueue(123123123123123123123123123123123)
