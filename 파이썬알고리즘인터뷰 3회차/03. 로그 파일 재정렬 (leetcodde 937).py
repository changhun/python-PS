class Solution:
    def reorderLogFiles(self, logs:list) -> list:
        char_logs = [log for log in logs if log[-1].isalpha()]
        num_logs = [log for log in logs if log[-1].isdigit()]
        char_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return char_logs + num_logs