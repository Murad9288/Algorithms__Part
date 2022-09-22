'''
    Best Sorting algorithms is Merge sort.
    Time Complexity     : O(n log n)
    Space Complexity    : O(n)
'''

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
