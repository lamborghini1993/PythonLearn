g = (i for i in range(5))
print(g, iter(g))
for x in g:
    print(x)

print("-" * 20)


def gen(n):
    for i in range(n):
        yield i


g = gen(6)
print(g, iter(g), type(g))
print("B:", next(g))
for x in g:
    print("A:", x)
