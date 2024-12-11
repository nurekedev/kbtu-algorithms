from timer import timing


def rearrange_array(arr):
    i = 0  
    j = len(arr) - 1
    
    while i < j:
        while i < len(arr) and arr[i] < 0:
            i += 1
        while j >= 0 and arr[j] >= 0:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [-3, 4, -2, 5, -1, 3, -4] 

rearrange_array(arr)

"""
    Inital array: [-3, 4, -2, 5, -1, 3, -4]
    1. Swap: arr[i]=4, arr[j]=-4 (i=1, j=6)
    After swap: [-3, -4, -2, 5, -1, 3, 4] 

    2. Swap: arr[i]=5, arr[j]=-1 (i=3, j=4)
    After swap: [-3, -4, -2, -1, 5, 3, 4] 

    No swap: i=4, j=3 (arr[i]=5, arr[j]=-1)    

    Result: [-3, -4, -2, -1, 5, 3, 4]
"""

@timing
def test_rearrange_array():
    rearrange_array(arr * 1000)

test_rearrange_array()