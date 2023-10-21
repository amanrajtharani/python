#Rotate array
arr = []
num = 0
for i in range(5):
    item = int(input("Enter element : "))
    arr.append(item)
rt_num = int(input("Enter the number from which you want to rotate : "))
for i in range(rt_num,len(arr)):
    for k in range(rt_num,len(arr)-1):
        if arr[i]<arr[k]:
            num = arr[i]
            arr[i] = arr[k]
            arr[k] = num

print(arr)
