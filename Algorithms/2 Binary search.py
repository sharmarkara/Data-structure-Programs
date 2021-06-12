def Binary_Search(Arr,low,high,x):
    if low<=high:
        mid=(low+high)//2

        if Arr[mid]==x:
            return mid
        elif Arr[mid]>x:
            return Binary_Search(Arr,low,mid-1,x)

        else:
            return Binary_Search(Arr,mid+1,high,x)


    else:
        return -1

Arr=[2, 3, 4, 10 , 40]
low=0
high=len(Arr)
x=40
Result=Binary_Search(Arr,low,high,x)

if Result!=-1:
    print("Element is present at index ",str(Result))

else:
    print("Element is not present in array")