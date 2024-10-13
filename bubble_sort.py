arr = [12, 45,23,16,7,9,13]
print(arr)

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j] 
            arr[j] = arr[j+1]
            arr[j+1]=temp

print(arr)