# 코드 4.3: 배열로 구현된 스택 클래스 (참고 파일: ch04/ArrayStack.py)
from ArrayStack import ArrayStack

s = ArrayStack(100)             # 스택 객체를 생성

msg = input("문자열 입력: ")    # 문자열을 입력받음
for c in msg :                  # 문자열의 각 문자 c에 대해
    s.push(c)                   # c를 스택에 삽입

print("문자열 출력: ", end='')
while not s.isEmpty():          # 스택이 공백상태가 아니라면
    print(s.pop(), end='')      # 하나의 요소를 꺼내서 출력
print()