def Input():
    result = []
    num = int(input(''))

    for i in range(num):
        result.append([])
        get = [int(b) for b in str(input('')).split(' ')]

        for k, a in enumerate(get):
            for _ in range(a):
                result[i].append(k + 1)

    return result

def solution(case):
    result = [0 for _ in range(len(case))]
    SortedCase = case
    for i in range(len(SortedCase)):
        if SortedCase[i] == 6:
            SortedCase[i] = 9
    SortedCase = list(reversed(SortedCase))
    SortedCase.sort(reverse=True)

    end = len(SortedCase) - 1
    start = 0

    for i in range(len(SortedCase)):
        if (i + 1) % 2 == 0:
            result[end] = SortedCase[i]
            end -= 1
        else:
            result[start] = SortedCase[i]
            start += 1

    return result

def main():
    get = Input()
    for a in get:
        result = solution(a)
        for b in result:
            print(str(b) + ' ', end='')
        print('')

main()
