def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        # Recursive call for both parts

        mergesort(left)
        mergesort(right)

        # Two iterators for traversing the two halves

        i=0
        j=0

        #Iterator for the main array or list

        k=0

        while i<len(left) and j <len(right):
            if left[i] <right[j]:
                # The value from the left half has been used
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i< len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

arr=[23,4,5,33,47,9,10,30,40,50]
mergesort(arr)
print(arr)



    