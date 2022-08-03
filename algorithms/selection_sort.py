import time

def selection_sort(data,speed,fn,*arg):
    inc_step = arg[0]
    for step in range(len(data)):
        minIndex=step
        for i in range(step,len(data)):
            if data[minIndex]>data[i]:
                minIndex = i
                inc_step()
            fn(data,["grey" if x==step else "green" if x==i else "blue" if x==minIndex else "black" for x in range(len(data))])
            time.sleep(speed)
        data[step],data[minIndex] = data[minIndex],data[step]
        #fn(data,["grey" if x==step else "green" if x==i else "pink" if x==minIndex else "black" for x in range(len(data))])




