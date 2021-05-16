def Input():
    CaseNum = int(input(''))
    Result = []

    for _ in range(CaseNum):
        Result.append([int(a) for a in str(input('')).split(' ')])

    return Result
def GetSize(n):
    i = 1
    while n >= 10 ** i:
        i += 1
    return i

def GetToN(n, a, b):
    return ((10 ** n) - a) // b

def Solution(case):
    # Setting Number Part
    a = case[0]
    b = case[1]
    c = case[2]

    start = GetSize(a)
    oldI = 0
    i = GetToN(start, a, b)
    # a + b(i - 1) < 10 ** (start)
    # bi < 10 ** (start) - a + b
    # i < ((10 ** start) - a) // b + 1

    while c > start * (i - oldI):
        c -= start * (i - oldI)
        oldI = i
        start += 1
        i = GetToN(start, a, b)

    i = GetToN(start - 1, a, b)
    if i < 0:
        i = 0


    # a + b(i - 1)
    q = c // start
    r = c % q
    i += q


    re = str(a + b * (i -1))
    return re[len(re) - 1 - r]



def main():
    Cases = Input()
    for Case in Cases:
        print(Solution(Case))

main()
