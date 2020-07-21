import sys

def Recursive_Binary(arr, l, r, k):
    assert len(a)<3 * (10**4)
    assert 1<=k<=10**9
    for i in a:
        assert 1<=i<=10**9
    if r>=l:
        mid= l + (r-l) //2

        if arr[mid]==k:
            return mid

        elif arr[mid]>k:
            return Recursive_Binary(arr, l, mid-1, k)

        else:
            return Recursive_Binary(arr, mid+1, r, k)

    else:
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
        print(Recursive_Binary(a, 0, len(a)-1, k), end = ' ')
