# 코드 4.5: 후위수식 계산 알고리즘 (참고 파일: ch04/EvalPostfix.py)
from ArrayStack import ArrayStack


def evalPostfix( expr ):
    s = ArrayStack(100)
    for token in expr :
        if token in "+-*/" :
            val2 = s.pop()
            val1 = s.pop()
            if   (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :
            s.push( float(token) )

    return s.pop()

if __name__ == "__main__":
    print('스택의 응용2: 후위표기식 계산\n')

    str1 =' 8 +2 / 3 - 3 2 * +'
    expr1 = str1.split()

    #expr1 = [ '8', '2', '/', '3', '-', '3', '2', '*', '+']
    expr2 = [ '1', '2', '/', '4', '*', '1', '4', '/', '*']

    print(expr1, ' --> ', evalPostfix(expr1))
    print(expr2, ' --> ', evalPostfix(expr2))

