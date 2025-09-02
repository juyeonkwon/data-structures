# 코드 5.10: 정렬되지 않은 배열을 이용한 우선순위 큐 클래스 (참고파일: ch05/PriorityQueue.py)
class PriorityQueue :
    def __init__( self, capacity = 10 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.size = 0                   # 후단의 인덱스

    def isEmpty( self ) :
        return self.size == 0

    def isFull( self ) :
        return self.size == self.capacity

    def enqueue( self, e ):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1

    def findMaxIndex( self ):
        if self.isEmpty(): return -1
        highest = 0
        for i in range(1, self.size) :
            if self.array[i] > self.array[highest] :
                highest = i
        return highest

    def dequeue( self ):
        highest = self.findMaxIndex()
        if highest != -1 :
            self.size -= 1 
            self.array[highest], self.array[self.size] = \
                self.array[self.size], self.array[highest]
            return self.array[self.size]

    def peek( self ):
        highest = self.findMaxIndex()
        if highest != -1 :
            return self.array[height]

    def __str__(self):
        return str(self.array[0:self.size])


# 코드 5.10: 원형 덱: 테스트 프로그램
if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue( 34 )
    q.enqueue( 18 )
    q.enqueue( 27 )
    q.enqueue( 45 )
    q.enqueue( 15 )

    print("PQueue:", q)
    while not q.isEmpty() :
        print("Max Priority = ", q.dequeue() )
