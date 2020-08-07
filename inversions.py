import sys
def merge_sort(arr):
    inversions=0
    n=len(arr)
    if n<=1:
        return inversions
    m=len(arr)//2
    left=arr[:m]
    right=arr[m:]
    inversions+=merge_sort(left)
    inversions+=merge_sort(right)
    i=j=k=0
    nl, nr = len(left), len(right)
    n=nl+nr

    while (i<nl and j<nr):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
            inversions+=(nl-i)
        k+=1

    if i>=nl:
        arr[k:] = right[j:]
    elif j>=nr:
        arr[k:] = left[i:]
    #print (arr)
    return inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a))
