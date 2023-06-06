from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        ans = []
        for person in sorted_people:
            ans.insert(person[1], person)
        return ans


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
ret = Solution().reconstructQueue(people)
print(ret)