def Input():
    CaseNum = int(input(''))
    Result = []

    for _ in range(CaseNum):
        Result.append([int(a) for a in str(input('')).split(' ')])

    return Result

def Solution(case):
    Num = ''
    a = case[0]
    b = case[1]
    c = case[2]

    i = 0
    while c > len(Num):
        Num += str(a + b * i)
        i += 1

    return Num[c-1]

def main():
    Cases = Input()
    for Case in Cases:
        print(Solution(Case))

main()