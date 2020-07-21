import sys

def BinarySearch2(a, k):
    #a is the given array, k is the key to search for

    assert len(a)<3 * (10**4)
    assert 1<=k<=10**9
    for i in a:
        assert 1<=i<=10**9
    #a.sort()   no need here because the inputs are already placed in sorted order
    upper_bound=len(a)-1
    lower_bound=0
    mid_pos=(len(a)//2)

    while lower_bound<=upper_bound:
        mid_pos=(upper_bound+lower_bound)//2
        if k==a[mid_pos]:
            return mid_pos
            #print ('the lower bound is', lower_bound)
        elif k<a[mid_pos]:
            upper_bound = mid_pos-1
            #print ('the upper bound is', upper_bound)
        else:
            #k>a[mid_pos]
            lower_bound=mid_pos+1


    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for k in data[n + 2:]:
        # replace with the call to binary_search when implemented
        assert 1<=k<=10**5
        print(BinarySearch2(a, k), end = ' ')
