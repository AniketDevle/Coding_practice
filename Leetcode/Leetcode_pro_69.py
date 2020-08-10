left = 0
right = 500000
x = 101
mid = int((left + right)/2)
while ( not (mid * mid <=x and (mid+1)*(mid+1) > x) ):
    
    if (mid*mid > x):
        right = mid
    elif (mid*mid == x):
        break
    else:
        left = mid
    mid = int((left + right)/2)

print(mid)    

    
