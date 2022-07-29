



class Node:
    def __init__(self , location=None  , data=None):
        self.location = location
        self.data = data
chess = {
    '00': Node(location='00' , data='Q1'),
    '01': Node(location='01'  ),
    '02': Node(location='02' ),
    '10': Node(location='10' , data='Q1'),
    '11': Node(location='11' ),
    '12': Node(location='12' ),
    '20': Node(location='20' ),
    '21': Node(location='21' ),
    '22': Node(location='22' , data='Q1'),
}
tempChess = {
    '0': {
        '0': Node(data='Q1'),
        '1': Node(),
        '2': Node()
    },
    '1' : {
        '0' : Node(data='Q2'),
        '1' : Node(),
        '2' : Node()
    },
    '2' : {
        '0' : Node(),
        '1' : Node(),
        '2' : Node(data='Q3')
    }
}
# for x in tempChess.keys():
#     for y in tempChess[x].keys():
#         print(tempChess[x][y].data)
#     print()



location = []
for x in tempChess.keys():
    for y in tempChess[x].keys():
        if tempChess[x][y].data != None:
            location.append((x + y))


print(location)