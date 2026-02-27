n, s = map(int, input().split())
 
nums = list(map(int, input().split()))
 
left = 0 
count = 0 
sum_ = 0 
 
for right in range(n):
  sum_ += nums[right]
 
  while sum_ >= s:
    count += n - right 
    sum_ -= nums[left]
    left += 1
 
 
print(count)
