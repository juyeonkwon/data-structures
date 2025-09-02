def printStep(arr, val) :
    print("  Step %2d = " % val, end='')
    print(arr)


# 코드 7.1: 선택 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if (A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]	    # 배열 항목 교환 
        printStep(A, i + 1);	            # 중간 과정 출력용 문장 

# 코드 7.2: 삽입 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)

# 코드 7.3: 버블 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        bChanged = False
        for j in range (i) :
            if (A[j]>A[j+1]) :
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True

        if not bChanged: break;			# 교환이 없으면 종료
        printStep(A, n - i);			# 중간 과정 출력용 문장


if __name__ == "__main__":
    org = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]

    data = list(org)
    print("Original  :", org)
    selection_sort(data)
    print("Selection :", data)

    data = list(org)
    print("Original  :", org)
    insertion_sort(data)
    print("Insertion :", data)

    data = list(org)
    print("Original  :", org)
    bubble_sort(data)
    print("Bubble    :", data)

