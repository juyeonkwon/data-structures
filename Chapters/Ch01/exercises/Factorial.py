# 코드 1.4: 반복 구조의 팩토리얼 함수
def factorial_iter(n) :
    result = 1
    for k in range(1, n+1) :	
        result = result * k	
    return result


# 코드 1.5: 순환 구조의 팩토리얼 함수
def factorial(n) :
    if n == 1 : 
        return 1
    else : 
        return n * factorial(n-1)


# 테스트 프로그램
n=3
print('Factorial순환 %d! ='%n, factorial(n))
print('Factorial반복 %d! ='%n, factorial_iter(n))
n=4
print('Factorial순환 %d! ='%n, factorial(n))
print('Factorial반복 %d! ='%n, factorial_iter(n))
n=5
print('Factorial순환 %d! ='%n, factorial(n))
print('Factorial반복 %d! ='%n, factorial_iter(n))


