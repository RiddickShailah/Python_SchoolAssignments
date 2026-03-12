def find_peak_index(arr):
    left, right = 0, len(arr)-1

    while left < right:
        mid = (left+right)//2
        if arr[mid]<arr[mid+1]:
            left=mid+1
        else:
            right=mid
    return left

arr1 = [0,1,0]
print(f'Arr1 = {arr1}, Expected: 1, Got: {find_peak_index(arr1)}')
arr2 = [0,10,5,2]
print(f'Arr2 = {arr2}, Expected: 1, Got: {find_peak_index(arr2)}')
arr3 = [3,5,7,9,11,8,6,4,2]
print(f'Arr3 = {arr3}, Expected 4, Got: {find_peak_index(arr3)}')