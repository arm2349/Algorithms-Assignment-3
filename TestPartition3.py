def Partition3(array, low, high):
    pivot=array[high]
    i=low-1
    k=high-1
    j=0
    #for j in range(low, high):

    #make sure k begins in correct place
    while array[k]==pivot:
        k-=1

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
                if array[k]<pivot:
                    array[j], array[k] = array[k], array[j]
                    while array[k]==pivot:
                        k-=1
                    i+=1
                    if array[i]>pivot:
                        array[i], array[j] = array[j], array[i]
                elif array[k]>pivot:
                    array[j], array[k] = array[k], array[j]
                    while array[k]==pivot:
                        k-=1
                else:
                    #this condition should never be met. Perhaps raising an exception is unnecessary,
                    #but i didn't know what else to put.
                    raise ValueError('array[k] should not be equal to pivot!')
                j+=1
    for _ in range (high-j+1):
        array[i+1], array[j] = array[j], array[i+1]
        j+=1
        i+=1
        if j>high:
            break
    #return i, j
    print (array)
    return array





import random
def TestPartition3():
    def lst_generator():
        for _ in range (50):
            l=[random.randint(1, 50) for i in range(10)]
            yield (l)

    get_lst=lst_generator()

    for i in get_lst:
        print (i)
        print ('After the partition: ')
        Partition3(i, 0, len(i)-1)
        print ('\n')

TestPartition3()
