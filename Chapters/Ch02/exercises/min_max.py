# 코드 2.1: 최솟값과 최댓값을 찾아 반환하는 함수

def find_min_max(A) :
    min = A[0]
    max = A[0]

    for i in range(1, len(A)) :
        if max < A[i] : max = A[i]
        if min > A[i] : min = A[i]

    return min, max



if __name__ == "__main__":
    data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
    x, y = find_min_max(data)
    
    print("(min,max) = ", (x,y))