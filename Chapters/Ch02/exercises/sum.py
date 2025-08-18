# 코드 2.2: 지정한 범위의 수를 합한 결과를 반환하는 함수

def sum_range(begin, end, step=1) :
    sum = 0
    for n in range(begin, end, step) :
        sum += n
    return sum


# 테스트 프로그램
if __name__ == "__main__":
    print("sum = ", sum_range(1, 10))
    print("sum = ", sum_range(1, 10, 2))