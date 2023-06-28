def f(N, S):
    return "\n".join([S] * N)


N = int(input())
S = input()

result = f(N, S)
print(result)
