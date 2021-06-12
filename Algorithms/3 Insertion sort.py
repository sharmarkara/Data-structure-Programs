#  Insertion sort is good for collections that are very small
#  or nearly sorted. Otherwise it's not a good sorting algorithm:
#  it moves data around too much.

#Time complexity is  Best O(n); Average O(n^2); Worst O(n^2)

def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>key:
                arr[j],arr[j+1]=arr[j+1],arr[j]

            else:
                arr[j+1]=key
                break

    return arr


arr=[2,9,4,3,5,7,4,8,9]
print(insertionSort(arr))

            