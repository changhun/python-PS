import collections

class Solution:


    def reorder(self, logs:list)->list:
        digits = []
        strs = []

        for s in logs:
            if s.split()[1].isdigit():
                digits.append(s)
            else:
                strs.append(s)
        strs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return strs+digits
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
sol = Solution()
print(sol.reorder(logs))


#split()
#sort(key=함수) => 여러 인자로 sorting
#lambda
#isdigit => 문자열이 숫자로 구성되었는지 판별하는 함수.
#print(logs[1].split()[1])