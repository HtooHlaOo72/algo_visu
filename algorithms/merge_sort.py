import math
import time

from utils.lib import calculate_speed
def merge(data,left,mid,right,speed,fn,inc_step,*arg): ##function to merge two sorted arrays 
    control = arg[0]
    
    
    left_len = mid-left+1
    right_len = right-mid
    sorted_arr = []
    l=r=0
    while l<left_len and r<right_len :
        control["condition"].acquire()
        inc_step()
        if(control["state"].get()):
            control["condition"].wait()
        control["condition"].release()
        if data[left+l] < data[mid+1+r]:
            sorted_arr.append(data[left+l])
            l+=1
        else:
            sorted_arr.append(data[mid+1+r])
            r+=1
        
    while l<left_len:
        inc_step()
        sorted_arr.append(data[left+l])
        l+=1
        
    while r<right_len:
        inc_step()
        sorted_arr.append(data[mid+1+r])
        r+=1
        
    k=0
    for x in range(left,right+1):
        data[x] = sorted_arr[k]
        k+=1
    fn(data,["green" if item>=left and item<=right else "black" for item in range(len(data))])
    time.sleep(calculate_speed(speed))

def merge_sort(data,l,r,speed,fn,inc_step,*arg):
    control = arg[0]
    control["condition"].acquire()
    if l<r:
        mid = l+(r-l)//2
        inc_step()
        if(control["state"].get()):
            control["condition"].wait()
        control["condition"].release()
        merge_sort(data,l,mid,speed,fn,inc_step,control)
        merge_sort(data,mid+1,r,speed,fn,inc_step,control)
        merge(data,l,mid,r,speed,fn,inc_step,control)
    return data