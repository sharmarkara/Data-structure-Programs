Arr=[11,2,10,5,6,78]

max=Arr[0]
min=Arr[0]
for i in range(1,len(Arr)):
    if Arr[i]<min:
        min=Arr[i]
    if Arr[i]>max:
        max=Arr[i]

print("Minimun element of an array is:",min)
print("Maximun element of an array is:",max)