t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    direction = input()
    
    pos = x
    first_zero = -1
    for i in range(min(k, n)):
        if direction[i] == "L":
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            first_zero = i + 1
            break
    
    if first_zero == -1 or first_zero > k:
        print(0)
        continue
    
    pos = 0
    cycle = -1
    for i in range(n):
        if direction[i] == "L":
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            cycle = i + 1
            break
    
    if cycle == -1:
        print(1) 
    else:
        resets = 1 + (k - first_zero) // cycle
        print(resets)
