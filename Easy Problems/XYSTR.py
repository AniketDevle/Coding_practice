testcase = int(input())
for _ in range(testcase):

    S = input()
    count = 0
    try:
        i = 0
        while(i < len(S)):
            if (S[i] != S[i+1]):
                count = count + 1
                i = i + 1
            i = i + 1
        print(count)
    except:
        print(count)
        
        
