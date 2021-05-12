def largest(arr,n):
    lar=arr[0]

    for i in range(1,n):
        if arr[i]>lar:
            lar = arr[i]

    return lar

arr=[2,99,44,8,809]
n=len(arr)
print("Largest elemet is",largest(arr,n))

