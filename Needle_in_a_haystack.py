from collections import Counter
 
test_cases = int(input())
 
for _ in range(test_cases):
  s = input()
  t = input()
 
  sc = Counter(s)
  tc = Counter(t)
 
  if not(sc <= tc):
    print("Impossible")
    continue 
 
  le = tc - sc
  left = []
 
  for e in le:
    while le[e] > 0:
      left.append(e)
      le[e] -= 1
 
  left.sort()
 
  res = []
  i = 0
  for e in s:
    while i < len(left) and left[i] < e:
      res.append(left[i])
      i += 1
    res.append(e)
 
  res.extend(left[i:])
  print(''.join(res))
