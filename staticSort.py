def swap(array, a, b):
    array[a], array[b] = array[b], array[a]

class MaxHeapSort:
    @staticmethod
    def siftDown(array, r, d, a):
        while r <= d // 2:
            l = 2 * r

            if l < d and array[a + l - 1] < array[a + l]:
                l += 1
            
            if array[a + r - 1] < array[a + l - 1]:
                swap(array, a + r - 1, a + l - 1)
                r = l
            else:
                break

    @staticmethod        
    def heapify(array, a, b):
        l = b - a
        i = l // 2
        while i >= 1:
            MaxHeapSort.siftDown(array, i, l, a)
            i -= 1
    
    @staticmethod
    def sort(array, a, b):
        MaxHeapSort.heapify(array, a, b)
        i = b - a
        while i > 1:
            swap(array, a, a + i - 1)
            MaxHeapSort.siftDown(array, 1, i-1, a)
            i -= 1
        
def uncheckedinsertionsort(array, a, b):
    for i in range(a + 1, b): 
        if array[i] < array[a]: 
            swap(array, i, a)

        key = array[i] 
        j = i-1
        
        while key < array[j]: 
            array[j+1] = array[j] 
            j -= 1
        array[j+1] = key

def findMinMax(array, a, b):
    currMin = array[a]
    currMax = array[a]
    for i in range(a + 1, b):
        if   array[i] < currMin:
            currMin = array[i]
        elif array[i] > currMax:
            currMax = array[i]
    return currMin, currMax

def staticSort(array, a, b):
    min_, max_ = findMinMax(array, a, b)

    auxLen = b - a

    count  = [0 for _ in range(auxLen + 1)]
    offset = [0 for _ in range(auxLen + 1)]

    CONST = auxLen / (max_ - min_ + 4)

    for i in range(a, b):
        count[int((array[i] - min_) * CONST)] += 1

    offset[0] = a

    for i in range(1, auxLen):
        offset[i] = count[i - 1] + offset[i - 1]

    for v in range(auxLen):
        while count[v] > 0:
            orig  = offset[v]
            from_ = orig
            num   = array[from_]

            array[from_] = -1

            while True:
                dig = int((num - min_) * CONST)
                to  = offset[dig]

                offset[dig] += 1
                count[dig]  -= 1

                tmp       = array[to]
                array[to] = num
                num       = tmp
                from_     = to

                if from_ == orig: break

    for i in range(auxLen):
        s = offset[i - 1] if i > 0 else a
        e = offset[i]

        if e - s <= 1:
            continue

        if e - s > 16:
            MaxHeapSort.sort(array, s, e)
        else:
            uncheckedinsertionsort(array, s, e)