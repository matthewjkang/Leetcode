s = "PAYPALISHIRING"
numRows = 4
mylist = []

for i in range(numRows):
    mylist.append([])

for i in range(len(s)):
    print(i%len(mylist))
    mylist[i%len(mylist)].append(s[i])
    if i%len(mylist) = 3:
        

print(mylist)
