import time
import random 
aThousandRandomNumbers = [random.randint(0,1000)]
for i in range(10000):
    aThousandRandomNumbers.append(random.randint(0,1000))
numbsss = [100, 101, 36, 201, 1]
def buble_sort(numbsss):
    for i in numbsss:
        for j in range(len(numbsss) -1):
            if numbsss[j] > numbsss[j+1]:
                storage = numbsss[j+1] 
                numbsss[j+1] = numbsss[j] 
                numbsss[j] = storage
    return numbsss
def insursino_sort(numbsss):
    for i in range(1, len(numbsss)):
        j = i - 1
        ki = numbsss[i]
        while ki < numbsss[j] and j > -1 :
            numbsss[j + 1] = numbsss[j]
            j = j -1 
            
        numbsss[j+1] = ki 
    return numbsss

# find smallest number and put to right off smallest number before it:
def selection_SORT(numbsss):
    for i in numbsss:  
        smallestNumber = numbsss[i]
        smallestPostition = i
        for j in range(i, len(numbsss)):
            if numbsss[j] < smallestNumber:
                smallestNumber = numbsss[j]
                smallestPosition = j
        storage = numbsss[i]
        numbsss[i] = smallestNumber
        numbsss[smallestPosition] = storage
        
    return numbsss

# deforestiation = partition
def deforestation(first,last,numbsss):
    PivotValue = numbsss[first]
    up = first + 1
    down = last
    while up < down:
        while numbsss[up] <= PivotValue and up != last:
            up = up + 1 
        while numbsss[down] > PivotValue and down != first:
            down = down - 1
        if up < down:
            storage = numbsss[up]
            numbsss[up] = numbsss[down]
            numbsss[down] = storage
    storage = numbsss[first]
    numbsss[first] = numbsss[down]
    numbsss[down] = storage
# up go up but when piv is > than up break -- nonsensical
    pivotIndex = down
    return pivotIndex

def quick_SORT(first,last,numbsss):          
    if first < last:
        pivotIndex = deforestation(first,last,numbsss)
        quick_SORT(first,pivotIndex-1, numbsss)
        quick_SORT(pivotIndex+1,last, numbsss)
    return numbsss

# copy = aThousandRandomNumbers.copy()
# start = time.time()
# buble_sort(copy)
# end = time.time()
# print ("it took ze sort of ze buble " + str(end-start) + " seconds to sort." + "uauauauauauajeidvmknbaghuijfk")

# copy =  aThousandRandomNumbers.copy()
# start = time.time()
# insursino_sort(copy)
# end = time.time()
# print ("it took insuSINO sort " + str(end-start) + " seconds to sort" + " ioajgoreibuha8tijrekfnsdbiguhjatewnshfbg")


# copy =  aThousandRandomNumbers.copy()
# start = time.time()
# selection_SORT(copy)
# end = time.time()
# print("it took selection SORT " + str(end-start) + " seconds to SORTTTT" + " ioajgihuyregffdsjnvdbhgjibkg hjer")


copy =  aThousandRandomNumbers.copy()
start = time.time()
quick_SORT(0,len(copy)-1,copy)
end = time.time()
print("it took quick SORT " + str(end-start) + " seconds to SORTTTT" + " ioajgihuyregffdsjnvdbhgjibkg hjer")

copy =  aThousandRandomNumbers.copy()
start = time.time()
copy.sort()
end = time.time()
print("it took PytHon Sort " + str(end-start) + " seconds to SORTTTT" + " ioajgihuyregffdsjnvdbhgjibkg hjer")