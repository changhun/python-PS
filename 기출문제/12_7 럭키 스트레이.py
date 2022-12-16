num = input()

length = len(num)
left_sum = 0
for i in range(length//2):
    left_sum += int(num[i])

right_sum = 0
for i in range(length//2, length):
    right_sum += int(num[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

# Input
# 7755
# 123402