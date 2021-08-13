def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = list(map(int,input().split()))
print("Before sort: ", arr)
bubbleSort(arr)
print("After Bubble sort: ",arr)


# 2nd rulse:
'''
def bubble_sort(L):
     n = len(L)
     for i in range(0, n):
          for j in range(0, n-i-1):
               if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    
L = list(map(int,input().split()))               
print("Before sort: ",L)
bubble_sort(L)
print("After Bubble sort: ",L)

'''



# 3rd rules:
'''

L = [2,4,1]
n = len(L)
for i in range(0, n):
    for j in range(0, n-i-1):
         if L[j] > L[j+1]:
               L[j], L[j+1] = L[j+1], L[j]
print(L)

'''
