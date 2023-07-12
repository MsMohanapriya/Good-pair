def good_pair(array,element_sum):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if(array[i]+array[j]==element_sum):
                return 1
    return 0

array=list(map(int,input().split()))
element_sum=int(input())
print(good_pair(array,element_sum))