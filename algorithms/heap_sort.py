
def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def parent(i):
    return i//2


def max_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)

    largest = i 

    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        # swap elements
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


def build_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)


def heap_sort(data):
    data.insert(0,None)
    build_max_heap(data)

    for i in range(len(data)-1, 1, -1):
        # swap elements
        data[i], data[1] = data[1], data[i]

        # after the swap the last element is now sorted, but the new root may break the max-heap condition
        # fix it by calling max-heapify with a smaller heap size (sorted elements are out of the picture)
        max_heapify(data, i, 1)

heap_sort([9,5,6,7,2,1,3,4,8])
