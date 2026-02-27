from collections import defaultdict 
n, k = map(int, input().split())
 
nums = list(map(int, input().split()))
 
left = 0 
count = 0 
freq = defaultdict(int)
 
for right in range(n):
  freq[nums[right]] += 1 
  
  while len(freq) > k:
    
    freq[nums[left]] -= 1 
    if freq[nums[left]] == 0 :
      del freq[nums[left]]
    left += 1
 
  count += right - left + 1
 
 
print(count)
