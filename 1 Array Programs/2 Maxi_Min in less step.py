def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    def partition(left, right, el):
        if left == right:
            return arr[left]
        pivot = arr[right]
        j = left - 1
        i = left
        m = 0
        while(i < right):
            if (arr[i] <= pivot):
                j += 1
                m += 1
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
        m += 1
        arr[j], arr[right] = arr[right], arr[j]
        if m == el:
            return arr[j]
        if m > el:
            return partition(left, j-1, el)
        return partition(j+1, right, el - m)
    return partition(l, r, k)


if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        print(kthSmallest(arr, 0, n-1, k))
        
