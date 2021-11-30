# Counting Sort:
# Myself Code:

arr = [6,5,7,8,1,4,3,2,9]
size = len(arr)
result = [0] * size
count = [0] * 10
for i in range(0,size):
    count[arr[i]] += 1
for i in range(1,10):
    count[i] += count[i - 1]
i = size - 1
while i >= 0:
    result[count[arr[i]] - 1] = arr[i]
    count[arr[i]] -= 1
    i -= 1
for i in range(0, size):
    arr[i] = result[i]
print("Counting Sort: %s"%arr)



# Counting sort in Python Programming.
# Outstanding 2nd system code:

'''
arr = [6,5,7,8,1,4,3,2,9]
size = len(arr)
result = [0] * size

# Initialize count list or array.
count = [0] * 10

# Store the count of each elements in count array or list.
for i in range(0,size):
    count[arr[i]] += 1

# Store the cummulative count.
for i in range(1,10):
    count[i] += count[i - 1]

# Find the index of each element of the original array in count array or list.
# place the elements in output array or list.
i = size - 1
while i >= 0:
    result[count[arr[i]] - 1] = arr[i]
    count[arr[i]] -= 1
    i -= 1

# Copy the sorted elements into original array or list.
for i in range(0, size):
    arr[i] = result[i]

# Counting sorted output the list or array.
print("Counting Sort: %s"%arr)

'''

# 3rd System.
# User Define Function use to counting sort:

# python program for counting sort
'''
def countingSort(arr):
    size = len(arr)
    out = [0] * size

    # count array initialization
    count = [0] * 10

    # storing the count of each element 
    for i in range(0, size):
        count[arr[i]] += 1

    # storing the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    i = size - 1
    while m >= 0:
        out[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        m -= 1

    for m in range(0, size):
        arr[i] = out[i]

arr = [3,5,1,6,7,8,3]
print("Counting Sort: %s"%(countingSort(arr)))

'''
