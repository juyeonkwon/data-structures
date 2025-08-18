# 코드 3.1: 배열로 구현된 리스트(함수버전) (참고 파일: ch03/ArrayListFn.py)

# 리스트의 데이터: 전역 변수
capacity = 100           # 리스트 용량: 예) 용량을 100으로 지정
array = [None]*capacity  # 요소 배열: [None, .., None] (길이가 capacity)
size = 0                 # 상단의 인덱스: 공백상태(-1)로 초기화 함


# 리스트의 연산: 일반 함수
def isEmpty( ) :
    if size == 0 : return True	# 공백이면 True 반환
    else : return False			# 아니면 False 반환

def isFull( ) :
    return size == capacity	    # 비교 연산 결과를 바로 반환

def getEntry(pos) :
    if 0 <= pos < size :
        return array[pos]
    else : return None

def insert( pos, e ) :
    global size                     # size는 전역변수
    if not isFull() and 0 <= pos <= size :
        for i in range(size, pos,-1) :
            array[i] = array[i-1]   # 한 칸씩 뒤로 옮김
        array[pos] = e              # pos위치에 새로운 요소 추가
        size += 1                   # 요소의 수가 하나 증가
    else : 
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

def delete( pos ) :
    global size                     # size는 전역변수
    if not isEmpty() and 0 <= pos < size :
        e = array[pos]
        for i in range(pos, size-1) :
            array[i] = array[i+1]   # 한 칸씩 앞으로 당김
        size -= 1                   # 요소의 수가 하나 감소
        return e
    else : 
        print("리스트 underflow 또는 유효하지 않은 삭제 위치")
        exit()

# 추가 연산들
def find(e) :
    for i in range(size) :
        if e == array[i] :
            return i
    return -1

def display(msg='ArrayList:' ):
    print(msg, array[0:size])



# 테스트 프로그램
if __name__ == "__main__":
    print("최초   ", array[0:size])
    insert(0, 10)
    insert(0, 20)
    insert(1, 30)
    insert(size, 40)
    insert(2, 50)
    print("삽입x5 ", array[0:size])
    delete(2)
    print("삭제(2)", array[0:size])
    delete(size-1)
    print("삭제(E)", array[0:size])
    delete(0)
    print("삭제(0)", array[0:size])