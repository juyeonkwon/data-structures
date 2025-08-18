# 코드 2.5: 자동차 클래스 (참고 파일: ch02/CarEx.py)

class Car :
    def __init__(self, color, speed = 0) :
        self.color = color
        self.speed = speed

    def speedUp(self) :
        self.speed += 10

    def speedDown(self) :
        self.speed -= 10

    # 2.11 연산자 중복
    def isEqual(self, carB) :
        if self.color == carB.color :
            return True
        else :
            return False

    def __eq__(self, carB) :
        return self.color == carB.color

    def __str__(self) :
        return "color = %s, speed = %d" % (self.color, self.speed)

    def display(self) :
        print(self.color, ":", self.speed)


if __name__ == "__main__":
    car1 = Car('black', 0)			# 검정색, 속도 0
    car2 = Car('red', 120)			# 빨간색, 속도 120
    car3 = Car('yellow')			# 노란색, 속도 0(디폴트 인수 사용)

    car1.display()
    car2.display()
    car3.display()

    car1.speedUp()		# car1 가속: 속도 10 증가 -> car1.speed는 10이 됨
    car2.speedDown()	# car2 감속: 속도 10 감소 -> car2.speed는 110이 됨

    car1.display()
    car2.display()


    # 2.11 연산자 중복 테스트

    car4 = Car('red', 0)
    
    print(car1.isEqual(car4))   # False
    print(car2.isEqual(car4))   # True
    print(car1==car4)           # False
    print(car2==car4)           # True
