

def check(arr , Num_string , Length):

    ##checking in  rows
    for i in arr:
        if 'spoon' in i:
            return True

    ##finding all possible string of columns
    brr = []    
    for i in range(Length):
        s = ""
        for j in range(Num_string):
            s = s + arr[j][i]
        brr.append(s)

    ##checking in columns    
    for i in brr:
        if 'spoon' in i:
            return True

    return False        

        


testcase = int(input())

for _ in range(testcase):

    Num_string , Length = [int(d) for d in input().split()]
    arr = []
    for i in range(Num_string):
        arr.append(input().lower())

    if(check(arr , Num_string , Length)):
        print("There is a spoon!")
    else:
        print("There is indeed no spoon!")
