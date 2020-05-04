"""

this is  one of the problems of the may challenge
#print minimum and maximum total cases possible
if distace between two patiens is less than or equal to 2 then he will infect others
1 2 5 6 7 
if 1 is infected he will infect 2 and rest of them will be safe so min = 2
if 5 is infected he will infect 6,7 so max = 3


This looks like a kaden's algorithm question

You got the solution question wrong 3 times cause you forgot to remove extra print
statements used while debugging

"""

def Minimum_possible_cases(li):
    min_possibles = []    
    if li[1] == 1:
        min_possibles.append(1)
    for i in range(1 , len(li)-1):
        if (li[i]>li[i-1] and li[i]>li[i+1]):
            min_possibles.append(li[i])
            continue
        if (li[i]<li[i-1] and li[i+1] == 1 ):
            min_possibles.append(li[i])
            continue

    min_possibles.append(li[len(li) -1])

    min_poss = sorted(min_possibles)
    
    return (min_poss[0] , min_poss[-1])
        
    
testcase = int(input())
for z in range(testcase):

    N = int(input())
    Arr = [int(d) for d in  input().split()]
    li = [1]
    for i in range(1,N):
        if (Arr[i]-Arr[i-1] <= 2):
            li.append(li[i-1] + 1)
        else:
            li.append(1)

    a,b = Minimum_possible_cases(li)
    print(a,b)
