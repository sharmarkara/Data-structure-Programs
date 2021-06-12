# Quick sort work on the basis of the pivot by selecting the 
# the elements left side of the pivot are smaller and the elements/
#right side the pivot elemet are the largest.

# Time complexity is : Best = Average =0(nlogn) , Worst=0(n^2)


def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]

    for j in range(low,high):
        if arr[j]<=pivot:

            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)

def quicksort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<high:

        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)


arr=[10,2,5,9,90,33]
n=len(arr)
quicksort(arr,0,n-1)
for i in range(n):
    print(arr[i],end=' ')
