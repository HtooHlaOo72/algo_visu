import time
def insertion_sort(data,speed,fn):
    for i in range(1,len(data)):
        temp=data[i]
        key=i-1
        while key>=0 and temp<data[key]:
            data[key+1]=data[key]
            key-=1
            fn(data,["blue" if x==key else "green" if x==i else "yellow" if x==key+1 else "black" for x in range(len(data))])
            time.sleep(speed)
        data[key+1]=temp
    print(data)
