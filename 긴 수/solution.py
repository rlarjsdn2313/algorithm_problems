def Input():
    CaseNum = int(input(''))
    Result = []

    for _ in range(CaseNum):
        Result.append([int(a) for a in str(input('')).split(' ')])

    return Result

# 10의 자리까지 10 / b
# 100의 자리까지 90 / b
# 1000의 자리까지 900 / b
# 10000의 자리까지 90000 / b
def GetHowMany(i, b):
    if i == 1:
        return 10 / b
    else:
        return (9 * (10 ** (i - 1))) / b

def Solution(case):
    # Setting Number Part
    a = case[0]
    b = case[1]
    c = case[2]

    d = 0
    i = 1
    while d < c:
        if a < 10 and i == 1:
            d += GetHowMany(i, b) * i
            i += 1

    # i - 1 자리 숫자에 있음
    e = 1
    while e < i - 1:
        c -= GetHowMany(e, b) * e
        e += 1

    if c % (i - 1) == 0:


    
    print(i)

def main():
    Cases = Input()
    for Case in Cases:
        print(Solution(Case))

main()