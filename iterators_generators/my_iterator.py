class MyFor(object):
    def __init__(self, start=0, end=5, step=1):
        self.cur = self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        print("call __iter__")
        return self
    
    def __next__(self):
        if self.cur >= self.end:
            raise StopIteration()
        result = self.cur
        self.cur += self.step
        return result
    
for i in MyFor(2, 10, 2):
    print(i)
