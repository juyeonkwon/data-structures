# 코드 4.1: 배열로 구현된 스택(함수버전) (참고 파일: ch04/ArrayStackFn.py)

capacity = 10            # 스택 용량: 예) 용량을 10으로 지정
array = [None]*capacity  # 요소 배열: [None, .., None] (길이가 capacity)
top = -1                 # 상단의 인덱스: 공백상태(-1)로 초기화 함

def isEmpty( ) :
    if top == -1 : return True	# 공백이면 True 반환
    else : return False			# 아니면 False 반환

def isFull( ) :
    return top == capacity	    # 비교 연산 결과를 바로 반환

def push( e ) :
    global top
    if not isFull() :		    # 포화상태가 아닌 경우
        top += 1			    # top 증가(global top 선언 필요)
        array[top] = e
    else :			            # 포화상태: overflow 
        print("stack overflow")
        exit()

def pop( ) :
    global top
    if not isEmpty():		    # 공백상태가 아닌 경우
        top -= 1			    # top 감소(global top 선언 필요)
        return array[top+1]
    else:			            # 공백상태: underflow 
        print("stack underflow")
        exit()

def peek( ) :
    if not isEmpty():		    # 공백상태가 아닌 경우
        return array[top]
    else: pass			        # underflow 예외는 처리하지 않았음


#  스택의 size() 연산
def size( ) : return top+1	    # 현재 요소의 수는 top+1


if __name__ == "__main__":
    msg = input("문자열 입력: ")     # 문자열을 입력받음
    for c in msg :                  # 문자열의 각 문자 c에 대해
        push(c)                   # c를 스택에 삽입

    print("문자열 출력: ", end='')
    while not isEmpty():          # 스택이 공백상태가 아니라면
        print(pop(), end='')      # 하나의 요소를 꺼내서 출력
    print()


