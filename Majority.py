import sys

def Majority(a):
    counts={}

    for i in a:
        counts.update({i:0})
    for i in a:
        if i in counts:
            counts[i]+=1
    #print (counts)
    val_lst=counts.values()
    for i in val_lst:
        if i>(len(a))/2:
            return 1
        else:
            continue
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if Majority(a) != -1:
        print(1)
    else:
        print(0)
