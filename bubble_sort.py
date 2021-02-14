# a = [2,44,23,45,77,1]
def bubble_sort(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                a[i],a[j] = a[j],a[i]
    print(a) 
bubble_sort([2,44,3,55,78,12])