class ProblemB(object):
    def __init__(self):
        #初始化数列计数器
        self.count = 0
        self._length = 0

    def length(self):
        return self._length

    def length(self, value):
        if not isinstance(value, int):
            raise ValueError("长度必须是整数哦~")
        if value < 1 or value > 100:
            raise ValueError("长度须在1〜100之间哦~")
        self._length = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.length:
            raise StopIteration()
        self.count = self.count + 1
        self.value = self.count * 2 - 1
        return self.value


def solution(sample):
    solu_iter = ProblemB()
    solu_iter.length = sample
    su = 0
    for i in solu_iter:
        su += i
    return su


print(solution(10))
