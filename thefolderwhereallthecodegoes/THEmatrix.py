from stacks_et_qs import Qew

class HIYAH:

    def __init__(self):  
        self.matrix = []
        i=0
        while i < 9:
            self.matrix.append([0,0,0,0,0,0,0,0,0])
            i = i+1

    def row_and_column_particular_one(self,row,column,value):
        self.matrix[row][column] = value
        self.matrix[column][row] = value 

    def removing_an_edge(self,row,column):
        self.matrix[row][column] = 0
        self.matrix[column][row] = 0 

    def pretty(self):
        for row in self.matrix:
            print(row)

    def checks_for_edge(self,row,column):
        return self.matrix[row][column] != 0

    def check_for_connections_to_the_row(self,rowindex):
        columnlist = []
        for i in range(0,len(self.matrix)):
            if self.checks_for_edge(rowindex,i):
                columnlist.append(i)
        return columnlist 

    def bread_thfirstsearch(self):
        start_vertex = 0
        queue = Qew()
        while 

whaaa = HIYAH() 
# print(whaaa.matrix)
whaaa.row_and_column_particular_one(6,7,1234)
print(whaaa.checks_for_edge(7,7))
whaaa.pretty()
print(whaaa.check_for_connections_to_the_row(6))