# Heap Sort in python

  def heapify(arr, n, i):
      # Find largest among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
  def heapSort(arr):
      n = len(arr)
  
      # Build max heap
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]
  
          # Heapify root element
          heapify(arr, i, 0)
  
  
  arr = [1, 12, 9, 5, 6, 10]
  heapSort(arr)
  n = len(arr)
  print("Sorted array is")
  for i in range(n):
      print("%d " % arr[i], end='')


# Heap Sorting 2nd rules:
'''
# কোনো Tree-নোডে right-চাইল্ডে কে আছে সেইটা দেখতে হলে (2*1) করতে হবে।
def left(i):
    return 2*i

# কোনো Tree-নোডে left-চাইল্ডে কে আছে সেইটা দেখতে হলে (2*i+1) করতে হবে।
def right(i):
    return 2*i+1

# কোনো Tree-নোডে parent কে আছে সেইটা দেখতে হলে (i//2) করতে হবে।
def parent(i):
    return i//2

def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)
    if l<= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap,heap_size,largest)

    if largest == i:
        return
    heap[i],heap[largest] = heap[largest],heap[i]

if __name__ == "__main__":
    h = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
    print(h)
    max_heapify(h,9,3)
    print(h)
    print()
    h = [None, 1, 2, 3]
    print(h)
    max_heapify(h , 3, 1)
    print(h)
'''
