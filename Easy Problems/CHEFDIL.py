"""
Whenever there are even number of integers in the binary then it is not
possible to win


1010 -> X110 -> X0X1  ##here the 0 in middle can never be over turned
          or -> XX00  ## both cards are facing upside down   


"""

testcases = int(input())

for z in range(testcases):
    S = input()
    Dict = {}
    for i in S:
        if i not in Dict.keys():
            Dict[i] = 0
        Dict[i] = Dict[i]+1
    if (Dict[str(1)] % 2 == 1):
        print("WIN")
    else:
        print("LOSE")

