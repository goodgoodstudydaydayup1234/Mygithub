from collections.abc import Iterator,Iterable


class Goods():
    def __init__(self, _addr):
        self.addr = _addr
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.addr):
            result = self.addr[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration()


g = Goods(['xinmi'])

try:
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)

print('end')

print(isinstance(g, Iterable))
print(isinstance(Goods, Iterable))
print(isinstance(g, Iterator))
print(isinstance(Goods, Iterator))
