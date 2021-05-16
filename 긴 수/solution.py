def Input():
    CaseNum = int(input(''))
    Result = []

    for _ in range(CaseNum):
        Result.append([int(a) for a in str(input('')).split(' ')])

    return Result

def GetHowBig(n):
    return len(str(n))

def Get(a, b, c):
    HowABig = GetHowBig(a)
    i = 2
    if HowABig == 1:
        c -= 9 // b

    d = (9 * (10 ** (i - 1))) // b
    # 9 * (10 ** (i - 1)) / b
    while d * i < c:
        if a >= 10 ** i:
            continue
        c -= d
        i += 1
        d = (9 * (10 ** (i - 1))) // b


    return [i, c]

def Solution(case):
    # Setting Number Part
    a = case[0]
    b = case[1]
    c = case[2]


    number, index = Get(a, b, c)

    l = 5
    i = 0
    R = a + b * i

    while True:
        if R >= 10 ** (number - 1):
            while not R >= 10 ** (number - 1):
                R = a + b * i
                print(R)
                i -= 1
            break
        else:
            R = a + b * i
            i += l
    
    i -= 1
    print(i)
    print (a + b * i)
    # while l <= c:
    #     R = str(a + b * i)
    #     print(R)
    #     l = len(R)
    #     c -= l
    #     i += 1

    # print(R)
    # return R[c - 1]

def main():
    Cases = Input()
    for Case in Cases:
        print(Solution(Case))

main()