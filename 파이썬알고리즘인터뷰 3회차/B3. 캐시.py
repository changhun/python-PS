import collections
MAX = int(1e5) + 5

def solution(cacheSize, cities):
    answer = 0
    counter = collections.Counter()
    if cacheSize == 0:
        return len(cities) * 5
    for i, city in enumerate(cities):
        if city.lower() not in counter:
            if len(counter) >= cacheSize:
                # correct?
                del counter[counter.most_common(1)[0][0]]
            counter[city.lower()] = MAX - i
            answer += 5
        else:
            counter[city.lower()] = MAX - i
            answer += 1

    return answer


cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cacheSize = 3
ret = solution(cacheSize, cities)
print(ret)