# Selection Sort:

L = list(map(int,input("Main List: ").split()))
N = len(L)
for i in range(0, N-1): # list er '0' number indexta baad diye porer gulo abar index akare dhorbe..
     index_min = i
     for j in range(i+1, N): # eikhane 'i+1' holo i er manta 1 kore barbe..
          if L[j] < L[index_min]:
               index_min = j
     if L[index_min] != i: # ei sortota dewar karon holo ekoy sonkha thakle oita r loop cholbena..
#   (if L[index_min] != i:) ei sortota na dilew hobe..
          L[i], L[index_min] = L[index_min], L[i] # ei line a odol-bodol kora hoyeche. eitake swaping bole...
print("After Selection sort: ", L)

# Selection sort 2nd rules..

'''
L = list(map(int,input().split()))
empty = []
n = len(L)-1
while n >= 0:
     for i in range(len(L)):
          if L[i] <= L[0]:
               L[0], L[i] = L[i], L[0]
     m = L.pop(0)
     empty.append(m)
     n -= 1
print(empty)
'''
