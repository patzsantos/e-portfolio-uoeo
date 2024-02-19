class TestClass:
    def sum(self, a, b, c):
        return a+b+c

    def sum(self, a, b):
        return a+b

obj = TestClass()
print(obj.sum(1,2))
