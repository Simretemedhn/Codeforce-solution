n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split())) 
p1 = 0 
p2 = 0 
count = 0

while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] < arr2[p2]:
        p1 += 1 
    elif arr1[p1] > arr2[p2]:
        p2 += 1
    else:
        val = arr1[p1]
        count_1 = 0
        count_2 = 0

        while p1 < len(arr1) and arr1[p1] == val:
            count_1 += 1
            p1 += 1
        while p2 < len(arr2) and arr2[p2] == val:
            count_2 += 1
            p2 += 1

        count += count_1 * count_2

print(count)
        


