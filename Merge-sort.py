
#MERGE-SORT IN PY
 
#EXPLANATION: 
#Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
#A problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.

#PESUDO-CODE:
#MergeSort(A, p, r):
#   if p > r 
#      return
#   q = (p+r)/2
#    mergeSort(A, p, q)
#   mergeSort(A, q+1, r)
#  merge(A, p, q, r)

# MergeSort in Python


def mergeSort(array):
    if len(array) > 1:

        #  d is where the arrays are divided into 2 parts.
        d = len(array)//2
        L = array[:d]
        M = array[d:]

        # Sorting the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Pick the largerest among the array,till we reach either end of either L or M.
        # Have to arrange elements of L & M in appropiate order.
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        #If elements are going exitint make sure to use remaining elements.
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


#now solving:😁
if __name__ == '__main__':
    array = [32, 121, 12122, 310, 39, 441]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
