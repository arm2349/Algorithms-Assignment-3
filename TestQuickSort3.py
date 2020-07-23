def Partition3(array, low, high):
    pivot=array[high]
    i=low-1
    k=high-1
    j=low
    #for j in range(low, high):
    while array[k]==pivot:
        k-=1
        if k==low:
            break
    while j<=k:
        if array[j]<pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
            j+=1

        elif array[j]>pivot:
            j+=1
        else:
            if j==k-1 and array[k]==pivot:
                j+=2
                break
            else:
                while array[k]==pivot:
                    k-=1
                    if k==low:
                        break
                if array[k]<pivot:
                    array[j], array[k] = array[k], array[j]
                    while array[k]==pivot:
                        k-=1
                        if k==low:
                            break
                    i+=1
                    if array[i]>pivot:
                        array[i], array[j] = array[j], array[i]
                elif array[k]>pivot:
                    array[j], array[k] = array[k], array[j]
                    #array[i+1], array[j] = array[j], array[i+1]
                    #i+=1
                    while array[k]==pivot:
                        k-=1
                        if k==low:
                            break
                else:
                    #this condition should never be met. Perhaps raising an exception is unnecessary,
                    #but i didn't know what else to put.
                    raise ValueError('array[k] should not be equal to pivot!')
                j+=1

    lower=i

    for _ in range (high-j+1):
        #print (array, j, i)
        array[i+1], array[j] = array[j], array[i+1]

        j+=1
        i+=1

        if j>high:
            break
    upper=i+1

    return lower, upper



def _quicksort3(array, low, high):
    if low<high:
        partition_index0=(Partition3(array, low, high)[0])
        partition_index1=(Partition3(array, low, high)[1])

        _quicksort3(array, low, partition_index0)
        _quicksort3(array, partition_index1, high)

def QuickSort3(arr):
    (_quicksort3(arr, 0, (len(arr))-1))


import random
def TestQuickSort3():
    def lst_generator():
        for _ in range (50):
            l=[random.randint(1, 50) for i in range(10)]
            yield (l)

    get_lst=lst_generator()

    for i in get_lst:
        print (i)
        print ('After the quicksort: ')
        QuickSort3(i)
        print (i)
        print ('\n')

TestQuickSort3()
