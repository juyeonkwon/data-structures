height = int(input("피라미드의 높이를 입력하세요: "))

for i in range(1, height+1) :
    for j in range(height-i) :
        print("   ", end='')            # 공백 출력

    for j in range(i) :
        print("%3d" % (j*2+1), end='')  # 증가하는 숫자 출력
        
    for j in range(i-2, -1, -1) :
        print("%3d" % (j*2+1), end='')  # 감소하는 숫자 출력

    print('')                           # 다음 줄로 이동