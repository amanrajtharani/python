arr = [1,43,8,3,12,76,2,98]
even = 0
odd = 0
num = 0
num2 = 0
for i in range(0,len(arr)-1):
    if i%2==0 or i==0:
       if arr[i]<arr[i+1]:
        even = arr[i]
        arr[i]= arr[i+1]
        arr[i+1] = even
        num += 1
    else:
       if arr[i+1]<arr[i]:
        odd = arr[i]
        arr[i]= arr[i+1]
        arr[i+1] = odd
        num2 += 1
print(num + num2)