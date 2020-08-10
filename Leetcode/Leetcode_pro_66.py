digits = [1 , 2 , 9]

best = digits[::-1]

print(best)

ans = []
rem = 1
counter = 0
for i in range(len(digits)):
    counter = i
    if (rem + best[i] > 9):
        ans.append((rem + best[i]) % 10)
    else:
        ans.append(rem + best[i])
        ans = ans + best[counter+1:]
        rem = 0
        break
        
if (rem == 1):
    ans.append(1)
        
print( ans[::-1])
