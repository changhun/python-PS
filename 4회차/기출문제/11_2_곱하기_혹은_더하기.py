s = input()
nums = [int(char) for char in s]
#print(nums)

ans = nums[0]
for num in nums[1:]:
    if ans > 1 and num > 1:
        ans *= num
    else:
        ans += num
print(ans)