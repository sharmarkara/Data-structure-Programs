#   Bubblesort is an elementary sorting algorithm. The idea is to
#   imagine bubbling the smallest elements of a (vertical) array to the
#   top; then bubble the next smallest; then so on until the entire
#   array is sorted. Bubble sort is worse than both insertion sort and
#   selection sort. It moves elements as many times as insertion sort
#   (bad) and it takes as long as selection sort (bad). On the positive
#   side, bubble sort is easy to understand. Also there are highly
#   improved variants of bubble sort.

# Time complexity is Best O(n^2); Average O(n^2); Worst O(n^2)

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1,i,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]

    return arr

arr=[19, 13, 6, 2, 18, 8]
print(bubblesort(arr))