
import time

def heapify(data, n, i, speed,fn, inc_step):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, speed,fn, inc_step)


def heap_sort(data, speed,fn, inc_step):
    n = len(data)
    for i in range(n-1, -1, -1):
        inc_step()
        heapify(data, n, i, speed,fn, inc_step)

    for i in range(n-1, 0, -1):
        inc_step()
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0, speed,fn, inc_step)
        fn(data, ["blue" if x == i else "black" for x in range(n)])
        time.sleep(speed)
    fn(data, ["black" for x in range(len(data))])
    