class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        for x in (self.a, self.b, self.c):
            if type(x) not in (int, float) or x <= 0: return 1
        if (self.a + self.b) <= self.c or (self.a + self.c) <= self.b or (self.b + self.c) <= self.a: return 2
        if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c) > self.a: return 3

a, b, c = map(int, input().split()) # эту строчку не менять

# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
