class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def show(self):
        print(f'({self.x}, {self.y})')
        
    def set(self, x, y):
        self.x = x
        self.y = y
        
    def get(self):
        return (self.x, self.y)


def show(self):
        x1, y1 = self.lt.get()
        x2, y2 = self.rb.get()
        print(f'좌측 상단 꼭지점이 ({x1}, {y1})이고 우측 하단 꼭지점이 ({x2}, {y2})인 사각형입니다.')
        
    def getWidth(self):
        return self.rb.x - self.lt.x

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')

