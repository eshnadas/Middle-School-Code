def binarySearch(list,left,right,value):
    #find the middle value in ur list
    middle = (left +(right-1))//2
    #check if left is right bc then the value is there
    if left == right:
        if list[left] == value:
            return left
        else:
            return -1 
    #checks if value is not in list
    elif right < left or left > right:
        return -1
    #checks if value is in middle  
    elif value == list[middle]:
        return middle 
    #removes everything after the value and change middle
    elif value < list[middle]:
        return binarySearch(list,left,middle-1,value)
    #removes everything before the value and change middle
    elif value > list[middle]:
        return binarySearch(list,middle+1,right,value)

#test function 
listt = [1,3,4,5,7,9,10,60123]
print(binarySearch(listt,0,len(listt)-1,6))