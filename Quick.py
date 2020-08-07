# Uses python3
import sys
import random

def Partition3(array, low, high):
    pivot=array[high]
    i=low-1
    k=high-1
    j=low
    if k==low and array[k]==pivot:
        return [low, high, True]
    #make sure k begins in correct place
    while array[k]==pivot:
        k-=1
        if k==low and array[k]==pivot:
            return [low,high,True]
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
        array[i+1], array[j] = array[j], array[i+1]
        j+=1
        i+=1
        if j>high:
            break
    upper=i+1
    return lower, upper

def _quicksort3(array, low, high):
    if low<high:
        partition_indices=(Partition3(array,low,high))
        partition_index0=partition_indices[0]
        partition_index1=partition_indices[1]
        if len(partition_indices)>2 and partition_indices[2]==True:
            return array

        _quicksort3(array, low, partition_index0)
        _quicksort3(array, partition_index1, high)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    assert 1<=n<=10**5
    for i in a:
        assert 1<=i<=10**9
    _quicksort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
