def CheckNum(n, win_nums):
    if n in win_nums:
        return True
    else:
        return False

def Get(lottos, win_nums):
    result = 0
    reserve = 0
    for l in lottos:
        if CheckNum(l, win_nums):
            result += 1
        elif l == 0:
            reserve += 1
    
    return [result + reserve, result]


def solution(lottos, win_nums):
    answer = []
    a = Get(lottos, win_nums)
    if a[0] < 2:
        answer.append(6)
    else:
        answer.append(7 - a[0])

    if a[1] < 2:
        answer.append(6)
    else:
        answer.append(7 - a[1])
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))