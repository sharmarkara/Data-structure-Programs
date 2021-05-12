# Range and coefficient of range of array

def getMin(arr,size):
    min=arr[0]
    for i in range(1,size):
        if arr[i]<size:
            min=arr[i]

    return min
def getMax(arr,size):
    max=arr[0]

    for i in range(0,size-1):
        if arr[i]>max:
            max=arr[i]

    return max


def getRange(arr,size):
    _Max=getMax(arr,size)
    _Min=getMin(arr,size)

    Range=_Max-_Min
    coefficientOFrange=Range/(_Max+_Min)
    print("The range is: ",Range)
    print("The coeffient of range is: ",coefficientOFrange)

if __name__=='__main__':

    arr=[5,10,24,1]
    size=len(arr)
    getRange(arr,size)