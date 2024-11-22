class Numbers():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
    
nums = Numbers()
itnums = iter(nums)

print(next(itnums))
print(next(itnums))
print(next(itnums))
print(next(itnums))
print(next(itnums))
print(next(itnums))