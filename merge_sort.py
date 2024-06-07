def merge_sort(lists):
    for i in range(len(lists)):
        for j in range(i+1, len(lists)):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists
           
lists = [20,10,90,45,26,73]     
result = merge_sort(lists)
print(result)
       
   