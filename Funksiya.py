
def get_fibonnachi_soni(n):
    arr = [ i for i in range(n)]
    arr[0] = 1
    arr[1] = 1
    i = 2
    while i != n:
        arr[i] = arr[i - 1] + arr[i - 2]
        i += 1
        if arr[i - 1] == n:
            return arr[i - 1]
    return arr
        
# print(get_fibonnachi_soni(13))      
        
    