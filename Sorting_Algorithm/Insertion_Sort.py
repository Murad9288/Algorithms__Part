# Insertion sorting
'''
L = [6,1,4,9,2]
n = len(L)
for i in range(1, n):
     item = L[i]
     j = i - 1
     while j >= 0 and L[j] > item:
          L[j+1] = L[j]
          j = j - 1
          L[j+1] = item
print("After Insertion sort: ",L)
'''
# 2nd System Insertion sorting..

def insertion_sort(L):
     n = len(L)
     for i in range(1,n):
          item = L[i]
          j = i - 1
          while j >= 0 and L[j] > item:
               L[j+1] = L[j]
               j = j - 1
               L[j+1] = item
               
L = list(map(int,input().split()))
print("Before list : ",L)
insertion_sort(L)
print("After Insertion sorting: ", L)

