def even_numbers(n):
    i = 0
    for i in range(n):
        if i % 2 == 0:
            yield i
for i in even_numbers(10):
    print(i)

def generators():
    yield 1
    yield 2
    yield 3
gen = generators()
print(next(gen))
print(next(gen))
print(next(gen))