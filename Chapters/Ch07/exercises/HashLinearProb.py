# 코드 7.11: 해시 테이블 및 해시 함수 준비
M = 13                  # 해시 테이블의 크기
table = [None]*M        # 해시 테이블. 모든 항목은 None으로 초기화


def hashFn(key) :     # 해시 함수로는 제산함수 사용
    return key% M

# 코드 7.12: 선형조사법의 삽입 연산
def insert(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == None or table[i] == -1 :
#        if table[i] == None :
            break               # 삽입 위치 발견
        i = (i + 1) % M         # 다음위치 조사
        count -= 1

    if count > 0 :              # 삽입할 곳이 있으면 삽입
        table[i] = key

# 코드 7.13: 선형조사법의 탐색 연산
def search(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == None :   # 탐색 실패
            return None
        if table[i] == key :    # 탐색 성공
            return table[i]
        i = (i + 1) % M
        count -= 1

    return None                 # 탐색 실패


# 코드 7.14: 선형조사법의 삭제 연산
def delete(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == key :    # 삭제할 레코드 발견
            table[i] = -1
#            table[i] = None
            return
        if table[i] == None :   # 삭제할 레코드 없음
            return
        i = (i + 1) % M
        count -= 1


# 코드 7.15: 선형조사법의 테스트 프로그램
if __name__ == "__main__":
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data :
        print( "h(%2d)=%2d"%(d,hashFn(d)), end=' ')
        insert(d)
        print(table)

    print("46탐색-->", search(46))
    print("39탐색-->", search(39))

    print("60삭제-->", end='')
    delete(60)
    print(table)
    print("46삭제-->", end='')
    delete(46)
    print(table)


