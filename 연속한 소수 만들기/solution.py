def CheckPrime(n):
    if n == 2:
        return True
    else:
        for i in range(2, int(n/2)):
            if n % i == 0:
                return False
    return True

def Solution(case):
    case = list(sorted(case))
    cases = []
    for a in case:
        for case
