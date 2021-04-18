# Binary Searching- 1
'''
def binary_search(L,i):
     left, right = 0, len(L)-1
     while left <= right:
          mid = (left + right)//2     # integer divison
          if L[mid] == i:
               return mid
          if L[mid] < i:
               left = mid + 1
          else:
               right = mid -1
     return -1
if __name__ == "__main__":
     L = [1,2,3,4,5,6,7,8]
     for  i in range(1,11):
          position = binary_search(L,i)
          if position == -1:
               if i in L:
                    print(i, "is in L, But function freturned -1")
               else:
                    print(i, "not in list")
          else:
               if L[position] == i:
                    print(i, "found in correct position.")
               else:
                    print("Binary search returned", position, "for", i,"which is incorrect")
     print("Program terminated")
'''
#Binary Searching - 2

L = list(map(int,input().split()))
print("Main List: ",L)
N = int(input())
left, right = 0, len(L) - 1
print("Total Length: ",right)
while left <= right:
     mid = (left + right)//2
     if L[mid] == N:
          print("Baniry Position: ",mid + 1)
          break
     elif L[mid] < N:
          left = mid + 1
          print("left position : ",left)
     else:
          right = mid - 1
          print("right position: ",right)
else:
     print("Sorry! %d Not found.: ",N)
