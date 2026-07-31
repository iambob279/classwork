def mergeSort(myList):
    #
    if len(myList) > 1:
        #Find the mid point of the list
        mid = len(myList) // 2
        #Create two new lists from myList, one containing the left half of the list and one containing the right 
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        #While there are items in both lists
        while i < len(left) and j < len(right):
            #If the next item in the left list is less than or equal to the next item in the right list
            if left[i] <= right[j]:
              #If there is more than 1 item in the list
              myList[k] = left[i]
              i += 1
            
            else:
                #
                myList[k] = right[j]
                j += 1

            k += 1

        
        #When either the left or the right list is empty, add all the remaining values in the other list to the new list
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)