def find_duplicate(num):
    n=len(num)

    max_idx,curr_max=0,0
    for i in range(n):
        id = num[i]%n
        num[id]+=n

    for i in range(n):
        if num[i]>curr_max:
            curr_max=num[i]

            max_idx=i

        num[i]%=n

    return max_idx

num=[4, 4, 5, 2, 3, 1,1]
print(find_duplicate(num))