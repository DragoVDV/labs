import sys

def size_m(N, W, H):
    # if not 1 <= N <= 1024 or not 1 <= W <= 10**9 or not 1 <= H <= 10**9:
    #     return None
    
    left = 1
    right = sys.maxsize
    size_of_board = -1

    while left <= right:
        mid = (left + right) // 2
        row = mid // W
        column = mid // H

        total_leaf = row * column

        if total_leaf >= N:
            size_of_board = mid 
            right = mid - 1
        else:
            left = mid + 1

    return size_of_board


