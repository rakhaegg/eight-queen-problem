data = {}

for x in range(8):
    value = 0
    for y in range(8):
        temp = str(x) + str(y)
        data[temp] = value
        value = value+1 

