# 코드 5.7: 파이썬 queue 모듈 테스트       참고파일: ch05/PythonQueue.py
import queue                # 파이썬의 큐 모듈 포함
Q = queue.Queue(maxsize=20) # 큐 객체 생성(최대크기 20)

for v in range(1, 10):
    Q.put(v)
print("큐의 내용: ", end='')
for _ in range(1, 10) :
    print(Q.get(), end=' ')
print()


Q = queue.LifoQueue(maxsize=20) # 스택 객체 생성(최대크기 20)

for v in range(1, 10):
    Q.put(v)
print("큐의 내용: ", end='')
for _ in range(1, 10) :
    print(Q.get(), end=' ')
print()