def romanToInt(string):
    numdict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    idx = 0
    sum = 0

    while idx != len(string):

        if string[idx:idx+2] in numdict and len(string[idx:idx+2]) ==2:
            sum += numdict[string[idx:idx+2]]
            idx += 2

        else:
            sum+= numdict[string[idx]]
            idx += 1

    return sum


print(romanToInt('IV'))