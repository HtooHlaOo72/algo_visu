import time
def insertion_sort(data,speed,fn,*arg):
    inc_step=arg[0]
    for i in range(1,len(data)):
        temp=data[i]
        key=i-1
        while key>=0 and temp<data[key]:
            inc_step()
            data[key+1]=data[key]
            key-=1
        data[key+1]=temp
        fn(data,["blue" if x==i else "green" if x==key+1 else "yellow" if x==key else "black" for x in range(len(data))])
        time.sleep(speed+0.3)
    fn(data,["black" for x in range(len(data))])
    print(data)

