n, k = map(int, input().split())
 
nums = list(map(int, input().split()))
 
from collections import defaultdict 
 
freq = defaultdict(int) 
left = 0 
right = 0
max_ = 0
m_l = 0
m_r = 0
while right < n:
    freq[nums[right]] += 1
 
    while len(freq) > k:
        freq[nums[left]] -= 1
        if freq[nums[left]] == 0:
            del freq[nums[left]]
        left += 1
 
    if right - left + 1 > max_:
        m_l = left + 1
        m_r = right + 1
        max_ = right - left + 1 
 
 
    max_ = max(max_, right - left + 1)     
    right += 1
 
print(m_l, m_r)
