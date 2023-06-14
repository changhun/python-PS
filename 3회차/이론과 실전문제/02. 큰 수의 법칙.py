n, m, k = map(int, input().split())
#print(n, m, k)

nums = list(map(int, input().split()))
#print(type(nums))
#print(nums)

nums.sort(reverse=True)
ans = 0
i = 0
q, r = m // (k + 1), m % (k + 1)
ans = (nums[0] * k + nums[1]) * q + nums[0] * r

print(ans)