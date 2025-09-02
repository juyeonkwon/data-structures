# 코드 7.7: 순차 탐색  알고리즘        참고 파일: ch07/basic_search.py
def sequential_search(A, key, low, high) :
    for i in range(low, high+1) :	# i에 low부터 high-1까지 순서대로 대입 
        print(A[i], end=' ')
        if A[i] == key :			# 탐색에 성공하면
            return i				# 인덱스 반환
    return -1						# 탐색에 실패하면 -1 반환 


# 코드 7.8: 이진 탐색  알고리즘(순환 구조)     참고 파일: ch07/basic_search.py
def binary_search(A, key, low, high) :
    if (low > high) :				# 종료 조건: 하나 이상의 항목이 있어야 함
        return -1        			# 탐색 실패

    middle = (low + high) // 2
    print(A[middle], end=' ')
    if (key == A[middle]) :	    # 탐색 성공
        return middle
    elif (key<A[middle]) :	# 왼쪽 부분리스트 탐색 
        return binary_search(A, key, low, middle - 1)
    else :						# 오른쪽 부분리스트 탐색 
        return binary_search(A, key, middle + 1, high)



# 코드 7.9: 이진 탐색  알고리즘(반복 구조)     참고 파일: ch07/basic_search.py
def binary_search_iter(A, key, low, high) :
    while (low <= high) :       	# 항목들이 남아 있으면(종료 조건)
        middle = (low + high) // 2
        print(A[middle], end=' ')
        if key == A[middle]:	    # 탐색 성공
            return middle
        elif (key > A[middle]):	# key가 middle의 값보다 크면 
            low = middle + 1		# middle+1 ~ high 사이 검색
        else:						# key가 middle의 값보다 작으면
            high = middle - 1		# low ~ middle-1 사이 검색
    return -1   					# 탐색 실패 


# 보간 탐색  알고리즘(순환 구조)     참고 파일: ch07/basic_search.py
def interpolation_search(A, key, low, high) :
    if (low > high) :				# 하나 이상의 항목이 있어야 탐색
        return -1        			# 탐색 실패

    middle = int(low + (high-low) * (key-A[low]) / (A[high]-A[low]))
    print(A[middle], end=' ')
    if (key == A[middle]) :	    # 탐색 성공
        return middle
    elif (key<A[middle]) :		# 왼쪽 부분리스트 탐색 
        return binary_search(A, key, low, middle - 1)
    else :						# 오른쪽 부분리스트 탐색 
        return binary_search(A, key, middle + 1, high)




if __name__ == "__main__":
    array = [ 2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47 ]
    n = len(array)

    print("입력배열 = ", array)
    key = 34
    print("순차탐색 %d: "%key, sequential_search(array, key, 0, n-1))
    print("이진탐색 %d: "%key, binary_search(array, key, 0, n-1))
    print("이진반복 %d: "%key, binary_search_iter(array, key, 0, n-1))
    print("보간탐색 %d: "%key, interpolation_search(array, key, 0, n-1))

    key = 23
    print("순차탐색 %d: "%key, sequential_search(array, key, 0, n-1))
    print("이진탐색 %d: "%key, binary_search(array, key, 0, n-1))
    print("이진반복 %d: "%key, binary_search_iter(array, key, 0, n-1))
    print("보간탐색 %d: "%key, interpolation_search(array, key, 0, n-1))

    array = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 100]
    key = 2
    print("보간탐색 %d: "%key, interpolation_search(array, key, 0, n-1))

