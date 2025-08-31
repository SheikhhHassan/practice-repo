# Searchin Algortihms: Used to find the that element exsists in data frame and where...

# Binary Search: Use in sorted Array. Half the array and if element is smaller go left, otherwise right.


def binary_search(arr, key):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1 
        else: 
            high = mid - 1
    return -1 


nums = [2, 4, 6, 8, 10, 12]
print(binary_search(nums, 12))                        