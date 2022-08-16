import time

def counting_sort(data, speed,fn, inc_step):
    n = max(data) + 1
    count = [0] * n
    for item in data:
        count[item] += 1
    
    k = 0
    for i in range(n):
        for j in range(count[i]):
            inc_step()
            data[k] = i
            fn(data, ["blue" for x in range(len(data))] )
            time.sleep(speed)
            k += 1

    fn(data, ["black" for x in range(len(data))])

