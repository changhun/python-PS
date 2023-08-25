from collections import deque
import collections


""" 
#리스트 for 문 돌면서 0번 인덱스 삭제
l = [1, 2, 3, 4, 5, 6]
for x in l:
    print(x)
    l.pop(0)
"""

"""
# 리스트는 for 문으로 loop 도는 중에 0 번 인덱스 삭제가 되는데, deque 는 안 됨.
q = deque([1, 2, 3, 4, 5, 6])
for x in q:
    print(x)
    q.popleft()
"""


"""
# deque 도 while 문으로 돌면 문제 없음. 
q = deque([1, 2, 3, 4, 5, 6])
while q:
    print(q[0])
    q.popleft()
"""


""" DefaultDict 테스트 """
adj = collections.defaultdict(deque)
for i in range(5):
    for j in range(i+1):
        adj[i].append(j)

"""
for i in range(5):
    print(adj[i])
"""

"""
#for x in adj:
#for x in adj.keys():
for x in adj.values():
    print(type(x))
    print(x)
"""

for key, value in adj.items():
    print(f'{key}: {value}')



# reversed 나 enumerate 는 iterator? 타입을 리턴하는 것 같다.
# iterator 타입은 list(iter_var) 을 통해 리스트로 만드는 게 가능한듯.
s = "abcdefg"
l = list(s)

#for char in reversed(s):
#    print(char)

reversed_l = list(reversed(s))
print(reversed_l)

reversed_l2 = list(reversed(l))
print(reversed_l2)

enum_l = list(enumerate(l))
print(enum_l)


# Counter most_common 보다 남아있는 개수 적으면 엔트리 개수만큼 출력한다.
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

counter = collections.Counter(tasks)
ret = counter.most_common(8)
print(len(ret))
print(ret)

ret = counter.most_common(7)
print(len(ret))
print(ret)

# dictionary 비어있는지 어떻게 확인해?
# len(dic) 이런식으로?
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
counter = collections.Counter(tasks)
print(len(counter))
if counter:
    print("counter")
for key in list(counter.keys()):
    del counter[key]

# dictionary 가 비어있으면 if 조건에 안 걸리는 듯
if not counter:
    print("no element")