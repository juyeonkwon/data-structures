# 코드 2.6: SuperCar 클래스 (참고 파일: ch02/SuperCar.py)

from Car import Car

class SuperCar(Car) :
    def __init__(self, color, speed = 0, bTurbo = True) :
        super().__init__(color, speed)
        self.bTurbo = bTurbo

    def setTurbo(self, bTurbo = True) :
        self.bTurbo = bTurbo

    def speedUp(self) :
        if self.bTurbo : 
            self.speed += 50
        else :
            super().speedUp()

    # str 연산자 중복
    def __str__(self) :
        if self.bTurbo :
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else :
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)


# 테스트 프로그램
if __name__ == "__main__":
    s1 = SuperCar("Gold", 0, True)
    s2 = SuperCar("White", 0, False)
    s1.speedUp()
    s2.speedUp()
    print("슈퍼카1:", s1)
    print("슈퍼카2:", s2)
