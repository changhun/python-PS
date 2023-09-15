import collections


def solution(str1, str2):
    answer = 0

    group1 = []
    group2 = []
    for i in range(1, len(str1)):
        if str1[i-1:i+1].isalpha():
            group1.append(str1[i-1:i+1].lower())

    for i in range(1, len(str2)):
        if str2[i-1:i+1].isalpha():
            group2.append(str2[i-1:i+1].lower())

    if not group1 and not group2:
        return 65536

    group1_size = len(group1)
    group2_size = len(group2)

    counter1 = collections.Counter(group1)
    counter2 = collections.Counter(group2)

    union_size = 0
    for key in counter1.keys():
        if key in counter2:
            union_size += min(counter1[key], counter2[key])
    total_size = group1_size + group2_size - union_size

    return 65536 * union_size // total_size

str1 = "FRANCE"
str2 = "french"
ret = solution(str1, str2)
print(ret)