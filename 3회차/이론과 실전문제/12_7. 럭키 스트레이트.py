s = input()
half = len(s)//2
nums = [int(c) for c in s]
if sum(nums[:half]) == sum(nums[half:]):
    print("LUCKY")
else:
    print("READY")