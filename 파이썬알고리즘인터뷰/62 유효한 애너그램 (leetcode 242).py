""" sol1(time out): insertion sort """
"""
class Solution:
    def insertion_sort(self, s: str) -> str:
        l = list(s)
        for i in range(1, len(s)):
            for j in range(i, 0, -1):
                if l[j-1] <= l[j]:
                    break
                l[j-1], l[j] = l[j], l[j-1]
        return ''.join(l)

    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = self.insertion_sort(s)
        sorted_t = self.insertion_sort(t)
        return sorted_s == sorted_t
"""

""" sol2: merge sort """
class Solution:
    def merge_sort(self, l: list, s: int, e: int) -> list:
        if s >= e:
            return

        #mid = s + (e - s) // 2
        mid = (s + e) // 2
        self.merge_sort(l, s, mid)
        self.merge_sort(l, mid+1, e)

        i, j = s, mid + 1
        tmp = []
        while i <= mid and j <= e:
            if l[i] <= l[j]:
                tmp.append(l[i])
                i += 1
            else:
                tmp.append(l[j])
                j += 1

        while i <= mid:
            tmp.append(l[i])
            i += 1
        while j <= e:
            tmp.append(l[j])
            j += 1
        for i in range(e - s + 1):
            l[s + i] = tmp[i]


    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        self.merge_sort(list_s, 0, len(list_s) - 1)
        self.merge_sort(list_t, 0, len(list_t) - 1)

        return list_s == list_t


s = "anagram"
t = "nagaram"
ret = Solution().isAnagram(s, t)
print(ret)