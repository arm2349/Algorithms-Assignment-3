def Majority_Tester(array):

    def freq_checker(arr):
        highest_count=arr.count(0)
        for i in arr:
            if arr.count(i)>=highest_count:
                highest_count=arr.count(i)
                most_frequent=i
        print ('the most frequently occurring number in', arr, 'is', most_frequent)
        return most_frequent
    ind=freq_checker(array)
    if array.count(ind)>len(array)/2:
        return 1
    else:
        return 0
    
