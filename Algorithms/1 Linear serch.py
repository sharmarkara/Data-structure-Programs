def Linear_Search(arr,n,element):
    for i in range(0,n):
        if arr[i]==element:
            print("Indes is",i)

    return -1
            
arr=[2,5,8,9,3,8,9]
n=len(arr)
element=8
print(Linear_Search(arr,n,element))