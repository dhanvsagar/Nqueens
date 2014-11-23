 
import numpy
 
class NQ:

    def __init__(self,n,callback):
        self.size = n
        self.columns = [] * self.size
        self.places = 0
        self.backtracks = 0
        self.callback = callback

    def place(self, startRow=0):
        self.callback(self.columns)
        if len(self.columns) == self.size:
            
            return self.columns

        
        else:
            for row in range(startRow, self.size): 
                if self.isSafe(len(self.columns), row) is True: 
                    self.columns.append(row)
                    self.places += 1 
                    return self.place()
 
            else: 
                lastRow = self.columns.pop()
                self.backtracks += 1 
                return self.place(startRow=lastRow + 1)

    def isSafe(self, col, row): 
        for threatRow in self.columns: 
            threatCol = self.columns.index(threatRow) 
            if row == threatRow or col == self.columns.index(threatRow):
                return False 
            elif threatRow + threatCol == row + col or threatRow - threatCol == row - col:
                return False 
        return True

def process(n):
     
    nqueens = NQ(n)
    nqueens.place(0)
    return nqueens.columns
 
'''cboard = numpy.array([[' '] * n] * n)
for queen in nqueens.columns:
    cboard[nqueens.columns.index(queen), queen] = 'Q'

print cboard'''
