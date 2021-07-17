def FindElement(array, e):
    for i, a in enumerate(array):
        if a == e:
            return i
    return -1

def solution(n, lost, reserve):
    answer = 0
    students = []
    for i in range(n):
        if i + 1 in reserve:
            if i + 1 in lost:
                students.append([i + 1, 1])
                lost.remove(i + 1)
                continue
            else:
                students.append([i + 1, 2])
                continue
        else:
            if i + 1 in lost:
                students.append([i + 1, 0])
                continue
            else:
                students.append([i + 1, 1])
                continue

    for ls in lost:
        i = 0
        i = FindElement(students, [ls - 1, 2])
        if i != -1:
            students[i][1] -= 1
            students[FindElement(students, [ls, 0])][1] += 1
            continue

        i = FindElement(students, [ls + 1, 2])
        if i != -1:
            students[i][1] -= 1
            students[FindElement(students, [ls, 0])][1] += 1
            continue

    for i in students:
        if i[1] >= 1:
            answer += 1
            
    return answer

print(solution(3, [3], [1]))