# Linear Searching
'''
for _ in range(int(input())):
    n = input()
    c = n.lower()
    L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in  range(len(L)):
        if L[i] == c:
            print(i+1)
            break
    else:
        print("Sorry")
'''
# Def Function use to Linear Searching..
'''
def linear_search(l,x):
     x2 = x.lower()
     n = len(l)
     i =0
     while i < n:
          if l[i] == x2:
               return i+1   # Eikhane i+1 dewar karonta holo index akare ber na howa..
          i += 1
     i = -1
     return i
while True:
     l = L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     x = input()
     print(linear_search(l,x))
'''
