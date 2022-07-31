import math
import time
def merge(data,left,mid,right,speed,fn): ##function to merge two sorted arrays 
    left_len = mid-left+1
    right_len = right-mid
    sorted_arr = []
    l=r=0
    while l<left_len and r<right_len :
        if data[left+l] < data[mid+1+r]:
            sorted_arr.append(data[left+l])
            l+=1
        else:
            sorted_arr.append(data[mid+1+r])
            r+=1
        
    while l<left_len:
        sorted_arr.append(data[left+l])
        l+=1
        
    while r<right_len:
        sorted_arr.append(data[mid+1+r])
        r+=1
        
    k=0
    for x in range(left,right+1):
        data[x] = sorted_arr[k]
        k+=1
    fn(data,["green" if item>=left and item<=right else "black" for item in range(len(data))])
    time.sleep(speed)

def merge_sort(data,l,r,speed,fn):
    if l<r:
        mid = l+(r-l)//2
        merge_sort(data,l,mid,speed,fn)
        merge_sort(data,mid+1,r,speed,fn)
        merge(data,l,mid,r,speed,fn)
    return data