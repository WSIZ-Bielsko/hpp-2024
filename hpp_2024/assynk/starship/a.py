class A:
    class Sub:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def __init__(self, x, y):
        self.s = self.Sub(1, 2)


if __name__ == '__main__':
    a = A(1,2)
    print(a.s.x)