import time

def bubble_sort(data,speed,fn,*arg):
    length = len(data)
    inc_step=arg[0]
    for i in range(length-1):
        for j in range(len(data)-i-1):
            print(speed,"Speed in algo")
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
            inc_step()
            fn(data,["blue" if x==j else "green" if x==j+1 else "red" if x>=len(data)-i else  "black" for x in range(len(data))])
            time.sleep(speed)
    fn(data,["red" for x in range(len(data))])

