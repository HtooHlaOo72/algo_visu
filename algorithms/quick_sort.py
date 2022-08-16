import time

def partition(data, start, end, inc_step):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        inc_step()
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort(data, start, end, speed,fn,inc_step):
    if start < end:
        inc_step()
        pivot_position = partition(data, start, end, inc_step)
        quick_sort(data, start, pivot_position-1, speed, fn,inc_step)
        quick_sort(data, pivot_position+1, end, speed,fn, inc_step)
        fn(data, ["purple" if x >= start and x < pivot_position else "yellow" if x == pivot_position
                        else "black" if x > pivot_position and x <=end else "blue" for x in range(len(data))])
        time.sleep(speed)
        
    fn(data, ["black" for x in range(len(data))])
