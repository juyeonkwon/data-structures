M = 13                  # 해시 테이블의 크기
table = [None]*M        # 해시 테이블. 모든 항목은 None으로 초기화

def hashFn(key) :     # 해시 함수로는 제산함수 사용
    return key% M

class Node:
    def __init__( self, data, link=None ):
        self.data = data
        self.link = link

# 코드 7.16: 체이닝을 이용한 오버플로 처리
def insert(key) :
    k = hashFn(key)     # 해시 주소 계산
    n = Node(key)       # 새로운 노드 생성
    n.link = table[k]   # 노드의 다음 노드로 시작 노드 연결
    table[k] = n        # 새로운 노드가 시작 노드가 됨

def search(key) :
    k = hashFn(key)
    n = table[k]                # 시작 노드
    while n is not None:        # 연결된 모든 노드를 탐색
        if n.data == key :      # 탐색 성공. 노드의 데이터(레코드) 반환
            return n.data
        n = n.link              # 링크를 따라 다음 노드로 진행
    return None                 # 탐색 실패. None 반환

def delete(key) :
    k = hashFn(key)
    n = table[k]                # 시작 노드
    before = None               # 이전 노드
    while n is not None:        # n이 None이 아닐때 까지
        if n.data == key :      # 삭제할 레코드 찾음
            if before == None : # 삭제할 항목이 시작 노드이면, 다음 노드가 시작노드
                table[k] = n.link
            else :              # 두 번째 이후 항목 삭제인 경우
                before.link = n.link
            return
        before = n
        n = n.link


def printTable() :
    for i in range(M):
        n = table[i]
        if n != None :
            print("[%2d] "% i, end='')
            while n is not None :
                print( n.data, end=' ')
                n = n.link
            print()

if __name__ == "__main__":
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data :
        insert(d)
    printTable()

    print("46탐색-->", search(46))
    print("39탐색-->", search(39))

    print("60삭제-->")
    delete(60)
    print("46삭제-->")
    delete(46)
    printTable()

