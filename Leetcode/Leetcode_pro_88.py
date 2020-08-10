arr = [ 1 , 1 ,  0 , 0 , 0]
arr2 = [ 1 , 3 , 14]

m = 2
n = 3

pos1= m-1
pos2= n -1
pos = m + n -1
while (pos1 >= 0 and pos2 >=0):
    if (arr[pos1] >= arr2[pos2]):
        arr [pos]= arr[pos1]
        pos1 = pos1 - 1
        pos = pos - 1
    else:
        arr[pos] = arr2[pos2]
        pos2 = pos2-1
        pos = pos - 1


if (pos1 == -1):
    arr[:pos2+1] = arr2[:pos2+1]


print(arr)        
