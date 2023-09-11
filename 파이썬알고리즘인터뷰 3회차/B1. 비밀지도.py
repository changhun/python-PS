def solution(n, arr1, arr2):
    answer = []
    or_value = []
    for i in range(n):
        oring = arr1[i] | arr2[i]
        s = []

        for _ in range(n):
            if oring & 1:
                s.append("#")
            else:
                s.append(" ")
            oring >>= 1
        s.reverse()
        answer.append("".join(s))

    return answer


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
ret = solution(len(arr1), arr1, arr2)
print(ret)
