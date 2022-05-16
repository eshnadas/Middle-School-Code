from stacks_et_qs import Qew
from stacks_et_qs import stack
class HIYAH:

    def __init__(self):  
        self.matrix = []
        i=0
        while i < 9:
            self.matrix.append([0,0,0,0,0,0,0,0,0])
            i = i+1

#adds edges
    def row_and_column_particular_one(self,row,column,value):
        self.matrix[row][column] = value
        self.matrix[column][row] = value 

#removes edges
    def removing_an_edge(self,row,column):
        self.matrix[row][column] = 0
        self.matrix[column][row] = 0 

#makes it look like grid 
    def pretty(self):
        for row in self.matrix:
            print(row)

#checks for edge
    def checks_for_edge(self,row,column):
        return self.matrix[row][column] != 0

#checks for stuff next to it 
    def check_for_connections_to_the_row(self,rowindex):
        columnlist = []
        for i in range(0,len(self.matrix)):
            if self.checks_for_edge(rowindex,i):
                columnlist.append(i)
        return columnlist 

#creates queue to check 4
    def Bread(self):
        startvertex = 0 
        queue = Qew()
        queue.enqueue(startvertex)
        tracker = [False]*9
        tracker[startvertex] = True
        while queue.isempty() == False:
            u = queue.front()
            queue.dequeue()
            for vertex in self.check_for_connections_to_the_row(u):
                if tracker[vertex] == False:
                    queue.enqueue(vertex)
                    tracker[vertex] = True

    def depfth(self):
        startdepfth = 0 
        the_stack = stack()
        the_stack.push(startdepfth)
        tracker = [False]*9
        tracker[startdepfth] = True
        while the_stack.isempty() == False:
            u = the_stack.peek()
            the_stack.pop()
            for vertex in self.check_for_connections_to_the_row(u):
                if tracker[vertex] == False:
                    the_stack.push(vertex)
                    tracker[vertex] = True


whaaa = HIYAH() 
#creates matrix
whaaa.row_and_column_particular_one(0,1,1)
whaaa.row_and_column_particular_one(1,2,1)
whaaa.row_and_column_particular_one(2,3,1)
whaaa.row_and_column_particular_one(2,8,1)
whaaa.row_and_column_particular_one(3,4,1)
whaaa.row_and_column_particular_one(4,5,1)
whaaa.row_and_column_particular_one(5,6,1)
whaaa.row_and_column_particular_one(6,7,1)
whaaa.row_and_column_particular_one(7,8,1)
whaaa.row_and_column_particular_one(7,3,1)
#whaaa.Bread()

print(whaaa.checks_for_edge(7,7))
whaaa.pretty()
print(whaaa.check_for_connections_to_the_row(6))
