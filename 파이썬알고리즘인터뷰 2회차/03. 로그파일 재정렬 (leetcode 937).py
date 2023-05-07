class Solution:
    def reorderLogFiles(self, logs:list) -> list:
        string_logs = [log for log in logs if log[-1].isalpha()]
        num_logs = [log for log in logs if log[-1].isnumeric()]
        string_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return string_logs + num_logs


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
ret = Solution().reorderLogFiles(logs)
print(ret)
