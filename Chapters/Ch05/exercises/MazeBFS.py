from CircularQueue import *

def isValidPos(x, y) :		# (x,y)가 갈 수 있는 방인지 검사하는 함수
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

# 코드 5.5: 너비우선탐색으로 미로의 출구를 찾는 함수       참고파일: ch05/MazeBFS.py
def BFS() :
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS: ')

    while not que.isEmpty(): 
        here = que.dequeue()
        print(here, end='->')
        x,y = here
        if (map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : que.enqueue((x, y - 1))   # 상
            if isValidPos(x + 1, y) : que.enqueue((x + 1, y))   # 우
            if isValidPos(x, y + 1) : que.enqueue((x, y + 1))   # 하
            if isValidPos(x - 1, y) : que.enqueue((x - 1, y))   # 좌
        print(' 현재 큐  : ', que)	# 현재 스택 내용 출력
    return False


# 코드 5.6: BFS 미로찾기 테스트 프로그램       참고파일: ch05/MazeBFS.py
map = [ [ '1', '1', '1', '1', '1', '1' ],
	    [ 'e', '0', '1', '0', '0', '1' ],
	    [ '1', '0', '0', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '0', 'x' ],
	    [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6

result = BFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')
