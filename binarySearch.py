def BinarySearch(Arr,x):
    Arr_length = len(Arr)
    low = 1
    high = Arr_length-1
    mid = int(low+high/2)
    if Arr[mid] == x:
           print("Element found at index",mid)
    else:       
        for i in range(1,Arr_length):
           if Arr[mid] == x:
               print("Element found at index",mid,"=",Arr[mid])
               break
           elif Arr[mid] > x:
               mid = high -i
           elif Arr[mid] < x:
               mid = low + i
        if (i+1) == len(Arr):
                if Arr[i] != x:
                    print("Element x not found, x = ",x)
                   
        
                
BinarySearch([12,20,44,66,77,88],88)

        