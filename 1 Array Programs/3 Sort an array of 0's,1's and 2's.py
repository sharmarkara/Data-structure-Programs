
def sort012(arr,n):
    lo=0
    mid=0
    hig=n-1
    while(mid<=hig):
        if arr[mid]==0:
            arr[lo],arr[mid]=arr[mid],arr[lo]
            lo=lo+1
            mid+=1

        elif arr[mid]==1:
            mid=mid+1

        else:
            arr[mid],arr[hig]=arr[hig],arr[mid]
            hig=hig=-1

    return arr

def printarr(arr):
    for k in arr:
        print(k,end=',')

arr=[0,0,2,1,1]
n=len(arr)
sort012(arr,n)
printarr(arr)



