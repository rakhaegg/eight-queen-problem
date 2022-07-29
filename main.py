import numpy as np
from queue import Queue

class Node:
    def __init__(self , location):
        self.location = location
        self.data = None
        self.h = None
class ChessBoard:
    def __init__(self , panjang , lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.data = {}
        self.h = None 
        for x in range(self.lebar):
            for y in range(self.panjang):
                key = str(x) + str(y)
                self.data[key] = Node(location=(x , y))
    def getChessBoard(self):
        row = [ x  for x in range(self.lebar)]
        coloumn = [y for y in range(self.panjang)]
        print(self.data[str(row[1]) + str(coloumn[0])].data)
    def insertQueen(self , queen):
        for x in queen.keys():
            self.data[queen[x]].data = x
    def all_data(self):
        for x in self.data.keys():
            if self.data[x].data != None:
                print(self.data[x].location)
    def test(self):
        count = 0
        for x in self.data.keys():
            
            print(x)

chess = ChessBoard(8 , 8)
initial_queen = {
    'Q1' : '50',
    'Q2': '61',
    'Q3' : '72',
    'Q4' : '34',
    'Q5' : "44",
    'Q6' : "55",
    'Q7' : "66",
    'Q8' : "57",
}
chess.insertQueen(initial_queen)
#chess.all_data()
chess.test()


