def minDominoRotations(tops, bottoms):

    long = tops+bottoms
    potentials = []
    for i in range(1,7):
        if long.count(i) >= len(tops):
            potentials.append(i)
    
    if not potentials:
        return -1
    t,b = 0,0
    i = potentials[0]
    for j in range(len(tops)):
        if tops[j] != i and bottoms [j] != i:
            return -1
        elif tops[j] == i and bottoms[j] ==i:
            pass
        elif tops[j] == i:
            t += 1
        elif bottoms[j] == i:
            b += 1
    return min(t,b)
    
#TESTCASES
tops1=[2,1,2,4,2,2]
bots1=[5,2,6,2,3,2]
expected1 = 2

tops2=[3,5,1,2,3]
bots2=[3,6,3,3,4]
expected2 = -1

tops3=[1,2,1,1,1,2,2,2]
bots3=[2,1,2,2,2,2,2,2]
expected3 = 1

tops4=[3,3,3,3,3,3,3,3]
bots4=[2,2,2,2,2,2,2,2]

tops5=[3,3,3,3,2,2,2,2]
bots5=[2,2,2,2,3,3,3,3]

tops6 = [1,3,4,1,2,1,3,4]
bots6 = [1,3,1,2,2,1,4,4]
 
print(minDominoRotations(tops6,bots6))
