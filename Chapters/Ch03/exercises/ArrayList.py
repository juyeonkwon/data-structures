# 코드 3.3: 배열로 구현된 리스트 클래스  (참고 파일: ch03/ArrayList.py)

class ArrayList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__( self, capacity=100 ):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    # 리스트의 연산: 클래스의 메소드
    def isEmpty( self ):
        return self.size == 0

    def isFull( self ):
        return self.size == self.capacity

    def getEntry(self, pos) :
        if 0 <= pos < self.size :
            return self.array[pos]
        else : return None

    def insert( self, pos, e ) :
        if not self.isFull() and 0 <= pos <= self.size :
            for i in range(self.size, pos,-1) :
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else : pass

    def delete( self, pos ) :
        if not self.isEmpty() and 0 <= pos < self.size :
            e = self.array[pos]
            for i in range(pos, self.size-1) :
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else : pass

    def __str__( self ) :
        return str(self.array[0:self.size])


# 테스트
if __name__ == "__main__":
    L = ArrayList(50)
    
    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(L.size, 40)
    L.insert(2, 50)
    print("삽입x5 ", L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(L.size-1)
    print("삭제(E)", L)
    L.delete(0)
    print("삭제(0)", L)
