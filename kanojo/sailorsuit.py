def f():
    n = int(input())
    result = "_".join([input() for _ in range(n)])
    return result


output = f()
print(output)
