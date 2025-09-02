from PriorityQueue import PriorityQueue

def isValidPos(x, y) :		# (x,y)가 갈 수 있는 방인지 검사하는 함수
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False


import math
(ox,oy) = (5, 4)
def dist(x,y) :
    (dx, dy) = (ox-x, oy-y)
    return -math.sqrt(dx*dx + dy*dy)



# 코드 5.11: 전략적 미로 탐색 함수       참고파일: ch05/MazePQueue.py
def MySmartSearch() :
    q = PriorityQueue()
    q.enqueue((0,1,dist(0,1)))
    print('PQueue: ')

    while not q.isEmpty(): 
        here = q.dequeue()
        print(here[0:2], end='->')
        x,y,_ = here
        if (map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : q.enqueue((x, y - 1, dist(x, y - 1)))
            if isValidPos(x, y + 1) : q.enqueue((x, y + 1, dist(x, y + 1)))
            if isValidPos(x - 1, y) : q.enqueue((x - 1, y, dist(x - 1, y)))
            if isValidPos(x + 1, y) : q.enqueue((x + 1, y, dist(x + 1, y)))

        print('우선순위큐: ', q)

    return False


map = [ [ '1', '1', '1', '1', '1', '1' ],
	    [ 'e', '0', '1', '0', '0', '1' ],
	    [ '1', '0', '0', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '0', 'x' ],
	    [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6

result = MySmartSearch()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')
