a = [22,34,1,56,21,63]
for i in range(len(a)):
    min_ind = i
    for j in range(i+1,len(a)):
        if a[min_ind] > a[j]:
            min_ind = j
    a[i],a[min_ind] = a[min_ind] , a[i]
print(a)