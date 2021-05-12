def maximumsum(arr):
    maxsum=0
    cursum=0
    for i in range(0,len(arr)):
        cursum=cursum+arr[i]

        if (cursum>maxsum):
            maxsum=cursum

        if(cursum<0):
            cursum=0

    return maxsum

arr=[-5,4,6,-3,4,-1]
print(maximumsum(arr))