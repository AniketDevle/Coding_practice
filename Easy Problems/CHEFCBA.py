

li = [int(x) for x in input().split()]
li = sorted(li)

if li[0] * li[3] == li[1]*li[2]:
    print ("Possible")
else:
    print("Impossible")
