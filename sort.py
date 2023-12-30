class Sort():
    def mergeSort(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            Sort.mergeSort(arr, left, mid)
            Sort.mergeSort(arr, mid + 1, right)
            Sort.merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        # create temporary arrays
        L = [0] * n1
        R = [0] * n2

        # copy data to temporary arrays L[] and R[]
        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        # merge the temporary arrays back into arr[left..right]
        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # copy the remaining elements of L[], if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # copy the remaining elements of R[], if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def bubbleSort(arr):
        returnList = [0, 0]
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    returnList[1] += 1
                    arr[j], arr[j + 1] = arr[j+1], arr[j]
                returnList[0] += 1
        print("Sorted Array with Bubble sort:", arr)
        return returnList
    
    def partition(arr, beg, end):
        pivot = arr[end]
        i = beg - 1
        for j in range(beg, end):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[end] = arr[end], arr[i+1]
        return i + 1
    
    def quickSort(arr, low, high):
        if low < high:
            pIndex = Sort.partition(arr, low, high)
            Sort.quickSort(arr, low, pIndex-1)
            Sort.quickSort(arr, pIndex, high)
