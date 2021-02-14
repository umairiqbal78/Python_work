def insertionSort(arr): 
  
    
    for i in range(1, len(arr)): 
  
        check = arr[i] 
   
        current = i-1
        while current >= 0 and check < arr[current] : 
                arr[current + 1] = arr[current] 
                current -= 1
        arr[current + 1] = check 
    return arr
  

arr = [78,1,23,49,0]
print(insertionSort(arr))
