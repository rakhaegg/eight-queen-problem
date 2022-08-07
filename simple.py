from queue import Queue
import random
import sys
class Node:
    def __init__(self , data=None , location=None):
        self.data = data
        self.location = location
        self.utara = None
        self.selatan = None
        self.barat = None
        self.timur = None
        self.barat_laut = None
        self.timur_laut = None
        self.barat_daya = None
        self.tenggara = None

class ChessBoard:
    def __init__(self , panjang , lebar , initialState):
        self.panjang = panjang
        self.lebar = lebar
        self.data = {}
        self.utama = initialState.copy()
        self.initialState = initialState
        self.alreadyExplored = initialState.copy()
        for x in range(self.lebar):
            for y in range(self.panjang):
                if (str(x) + str(y)) in self.initialState:
                    self.data[str(x) + str(y)] = Node(data='Q'+ str(y+1), location=(x , y))
                else:
                    self.data[str(x) + str(y)] = Node(data=None, location=(x , y))
        for x in self.data.keys():
            x_int = int(x[0])
            y_int = int(x[1]) 
            if x_int == 0  and y_int == 0:
                self.data[x].selatan = self.data['10']
                self.data[x].timur = self.data['01']
                self.data[x].tenggara = self.data['11']
            if x_int == 0 and y_int != 0 and y_int != (self.panjang-1):
                self.data[x].barat = self.data[str(x_int)+str(y_int-1)]
                self.data[x].timur = self.data[str(x_int)+str(y_int+1)]
                self.data[x].tenggara = self.data[str(x_int+1)+str(y_int+1)]
                self.data[x].barat_daya = self.data[str(x_int+1)+str(y_int-1)]
                self.data[x].selatan = self.data[str(x_int+1) + str(y_int)]
            if x_int == 0 and y_int == (self.panjang-1):
                self.data[x].barat= self.data[str(x_int)+str(y_int-1)]
                self.data[x].selatan= self.data[str(x_int+1)+str(y_int)]
                self.data[x].barat_daya = self.data[str(x_int+1)+str(y_int-1)]
            if x_int != 0 and x_int != (self.lebar-1) and y_int == 0:
                self.data[x].utara= self.data[str(x_int-1)+str(y_int)]
                self.data[x].timur_laut = self.data[str(x_int-1)+str(y_int+1)]
                self.data[x].timur = self.data[str(x_int)+str(y_int+1)]
                self.data[x].tenggara = self.data[str(x_int+1) + str(y_int+1)]
                self.data[x].selatan = self.data[str(x_int+1) + str(y_int) ]
            if x_int != 0 and x_int != (self.lebar-1) and y_int != 0 and y_int != (self.panjang-1):
                self.data[x].utara = self.data[str(x_int-1) + str(y_int) ]
                self.data[x].timur_laut = self.data[str(x_int-1) + str(y_int+1)]
                self.data[x].timur = self.data[str(x_int) + str(y_int+1)]
                self.data[x].tenggara = self.data[str(x_int+1) + str(y_int+1)]
                self.data[x].selatan = self.data[str(x_int+1)+ str(y_int)]
                self.data[x].barat_daya = self.data[str(x_int+1) + str(y_int-1)]
                self.data[x].barat = self.data[str(x_int) + str(y_int -1 ) ]
                self.data[x].barat_laut = self.data[str(x_int-1) + str(y_int-1)]
            if x_int != 0 and x_int != (self.lebar-1) and y_int == (self.panjang-1):
                self.data[x].utara = self.data[str(x_int-1) + str(y_int)]
                self.data[x].barat_laut = self.data[str(x_int - 1) + str(y_int-1) ]
                self.data[x].barat =  self.data[str(x_int) + str(y_int-1)]
                self.data[x].barat_daya = self.data[str(x_int+1) + str(x_int-1)]
                self.data[x].selatan = self.data[str(x_int+1) + str(y_int)]
            if x_int == (self.lebar-1) and y_int == 0:
                self.data[x].utara = self.data[str(x_int-1) + str(y_int)]
                self.data[x].timur_laut = self.data[str(x_int-1) + str(y_int+1)]
                self.data[x].timur  = self.data[str(x_int) + str(y_int+1)]
            if x_int == (self.lebar -1 ) and y_int != 0 and y_int != (self.panjang-1):
                self.data[x].utara = self.data[str(x_int-1) + str(y_int )]
                self.data[x].timur_laut = self.data[str(x_int-1) + str(y_int+1)]
                self.data[x].timur = self.data[str(x_int) + str(y_int+1)]
                self.data[x].barat = self.data[str(x_int) + str(y_int-1)]
                self.data[x].barat_laut = self.data[str(x_int-1) + str(y_int-1)]
            if x_int == (self.lebar - 1) and y_int == (self.panjang -1):
                self.data[x].utara = self.data[str(x_int -1) + str(y_int)]
                self.data[x].barat_laut = self.data[str(x_int - 1) + str(y_int -1)]
                self.data[x].barat  = self.data[str(x_int) + str(y_int-1)]

    def checkKey(self , key , first , second , h):
        tmp = str(first) + str(second)
        if tmp not in key:
            key.append(tmp)
    
    def updateInitalState(self):
        while True:
            whichRow = str(random.randint(0,self.panjang-1))
            whichColumn = str(random.randint(0,self.panjang-1))
            temp = whichRow + whichColumn
            if temp not in self.alreadyExplored:                
                
                """
                
                """

                #print("Update Coloumn : " , temp)
                lastUpdate = self.alreadyExplored[len(self.alreadyExplored)-1]
                #print(lastUpdate)

                #print("Last Update : " , lastUpdate)
                #print("asdasd : " , self.utama[int(lastUpdate[1])])
                
                if lastUpdate != self.utama[int(lastUpdate[1])]:
                    self.data[lastUpdate].data = None
                    self.initialState[int(lastUpdate[1])] = self.utama[int(lastUpdate[1])]
                    
                    self.data[self.utama[int(lastUpdate[1])]].data = 'Q' + str(int(lastUpdate[1]) + 1)
                    
                #print(self.initialState)
                # ! Kolom atau queen mana yang akan di update
                whereColumn = int(whichColumn)
                
                # ! Pada dict queen lama data menjadi None agar tidak terdeteksi sebagai posisi queen
                #self.data[self.utama].data = None
                # ! Pada list queen ke berapakah yang akan diupdate posisitsi 
                #print("Update  : " , temp)
                sementerara = self.initialState[whereColumn]
                
                self.initialState[whereColumn] = temp
                # ! Update di dictionary
                #print("Sementara : " , sementerara)
                #print("Update :  " ,  temp)
                self.data[sementerara].data = None
                self.data[temp].data = 'Q' + str(whereColumn+1)
                
                #print("Update Location " , temp)
                #print("Coloumn : " , whereColumn)
                #print(self.initialState)
                #print(self.initialState)
                self.alreadyExplored.append(temp)
                #print(self.initialState)
                break     
                
    def estimateCost(self):
        key = []
        h = 0
        #print("State : " , self.initialState)
        for x in self.initialState:
            parent = self.data[x]
            #print("PARENT : " , parent.data)
            # print("X : " , x)
            # print("Parent : " , parent.data)
            # print("Location : " , parent.location)
            current_timur_laut = parent.timur_laut

            while current_timur_laut :
                
                if current_timur_laut.data != None:
                    #print("Timur Laut : " , current_timur_laut.data)
                    first = int(parent.data[1])
                    second = int(current_timur_laut.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)     

                current_timur_laut = current_timur_laut.timur_laut
            current_timur = parent.timur
            while current_timur:
                if current_timur.data != None:
                    #print("Timur  : " , current_timur.data)
                    first = int(parent.data[1])
                    second = int(current_timur.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)    
                current_timur = current_timur.timur
                
            current_tenggara = parent.tenggara
            while current_tenggara:
                if current_tenggara.data != None:
                    #print("Tenggara : " , current_tenggara.data)
                    first = int(parent.data[1])
                    second = int(current_tenggara.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)
                current_tenggara = current_tenggara.tenggara             
            current_barat = parent.barat
            while current_barat:
                if current_barat.data != None:
                    #print("Barat : " , current_barat.data)
                    first = int(parent.data[1])
                    second = int(current_barat.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)
                current_barat = current_barat.barat
            
            current_barat_laut = parent.barat_laut
            while current_barat_laut:
                if current_barat_laut.data != None:
                    #print("Barat Laut : " , current_barat_laut.data )
                    first = int(parent.data[1])
                    second = int(current_barat_laut.data[1])
                    if first < second:
                        self.checkKey(key , first , second,h)
                    else:
                        self.checkKey(key , second , first , h)
                current_barat_laut = current_barat_laut.barat_laut            
                        
            current_barat_daya = parent.barat_daya
            while current_barat_daya:
                if current_barat_daya.data != None:
                    #print("Barat Daya : " , current_barat_daya.data)
                    first = int(parent.data[1])
                    second = int(current_barat_daya.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)
                current_barat_daya = current_barat_daya.barat_daya
        return len(key) , key
            
            


class Data:
    def __init__(self , heuristic , pair,state):
        self.heuristic = heuristic
        self.pair  = pair
        self.state = state

def do_hill():
    initalState = ['40' , '51' , '62' , '33' , '44' , '55' , '66' , '57']
    global_max = []
    count = 0
    while True:
        chess = ChessBoard(panjang=8 , lebar=8 , initialState=initalState)
        data = {}
        # if len(global_max) > 2:
        #     if global_max[len(global_max) -1 ] == global_max[len(global_max) -2] == global_max[len(global_max) -3]:
        #         print(initalState)
        #         print(global_max[len(global_max)-1])
        #         print(global_max[len(global_max) -2])
        #         print(global_max[len(global_max) -3])

        #         break
        if len(global_max) != 0:
            if global_max[len(global_max)-1] == 1: 
                print(global_max[len(global_max)-1])
                break
        while True:
            if len(chess.alreadyExplored) == 16:
                break
            else:
                heuristic , pair = chess.estimateCost()
                dataDoneHeuristic = Data(heuristic=heuristic , pair=pair , state=chess.initialState.copy())
                data[dataDoneHeuristic] = heuristic
                #data_heuristic.append(heuristic)
                chess.updateInitalState()    
        local_max = sys.maxsize
        for x in data.keys():
            if data[x] <= local_max:
                local_max = data[x]
                initalState = x.state
        global_max.append(local_max)
        print("New State : " , initalState )
        count = count + 1
do_hill()
