def SeqSearch(Arr,x):
    for i in range(len(Arr)):
        if Arr[i] == x:
            print("Element found at index {}={}".format(i,Arr[i]))
            break
        elif (i+1) == len(Arr):
            if Arr[i] != x:
                print("Element not found")

SeqSearch([1,2,3,4,55],55)        