# 2.11 도전 코딩

class Car :
    def __init__(self, color, speed = 0) :
        self.color = color
        self.speed = speed

    def speedUp(self) :
        self.speed += 10

    def speedDown(self) :
        self.speed -= 10

    def __lt__(self, carB) :
        return self.speed < carB.speed

    def __gt__(self, carB) :
        return self.speed > carB.speed

    def __str__(self) :
        return "color = %s, speed = %d" % (self.color, self.speed)


if __name__ == "__main__":
    car1 = Car('black', 0)			# 검정색, 속도 0
    car2 = Car('red', 120)			# 빨간색, 속도 120

    print("car1:", car1)
    print("car1:", car2)

    print("car1 < car2 : ", car1 < car2)
    print("car1 > car2 : ", car1 > car2)
