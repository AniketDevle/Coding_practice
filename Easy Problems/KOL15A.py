
testcases = int(input())
for z in range(testcases):
    St = input()
    dictionary = {}
    for i in St:
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] += 1
    sum1 = 0
    for i in range(1,10):
        if str(i) in dictionary:
           sum1 = sum1 + dictionary[str(i)] * i
    print(sum1)
        
    
