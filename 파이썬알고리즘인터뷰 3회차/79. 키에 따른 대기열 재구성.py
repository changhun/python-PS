from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x: (-x[0], x[1]))

        for person in people:
            ans.insert(person[1], [person[0], person[1]])

        return ans


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
ret = Solution().reconstructQueue(people)
print(ret)