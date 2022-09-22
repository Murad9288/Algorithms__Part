'''
    Best Sorting algorithms is Merge sort.
    Time Complexity     : O(n log n)
    Space Complexity    : O(n)
'''
# First System:
# Merge sorting is simple code:
# Python program for implementation of MergeSort

def merge(left,right):
    merged_list = []
    L,R = len(left),len(right)
    i,j = 0,0

    # Now checking left and right sorting and Copy data to temp arrays L[] and R[]
    while i < L and j < R:
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # Checking if any element was left
    if i < L:
        merged_list += left[i:] # merge_list Add elements to the list.

    # Checking if any element was left
    elif j < R:
        merged_list += right[j:]  # merge_list Add elements to the list.
    return merged_list

# Now merge sorting:
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    # Finding the mid of the array
    mid = len(arr)//2

    # Dividing the array left and right elements
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

# input list:
arr = [[4,7,2,3],[23,45,3],[4,55,6,7,5][3],[5,1],[1,4]]
for i in arr:
    sorted_list = merge_sort(i)
    print("Original List:",i)
    print("Sorted List:",sorted_list)
    print()
    
# output:
'''
Original List: [4, 7, 2, 3]
Sorted List: [2, 3, 4, 7]

Original List: [23, 45, 3]
Sorted List: [3, 23, 45]

Original List: [4, 55, 6, 7, 5]
Sorted List: [4, 5, 6, 7, 55]

Original List: [3]
Sorted List: [3]

Original List: [5, 1]
Sorted List: [1, 5]

Original List: [1, 4]
Sorted List: [1, 4]

program finished <<<--
'''



# Second Sytem:

# Python program for implementation of MergeSort
def mergeSort(list):
    arr = list
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Now checking left and right sorting and Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # Checking if any element was right
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Driver Code
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print("Given array is ->:",end=" ")
    print(*arr)
    print("Sorted array is ->:",end=" ")
    print(*mergeSort(arr))
    
    
    
    
