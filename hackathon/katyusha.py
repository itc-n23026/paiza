def f(n, p, m, q):
    total_cost = (n * p) + ((n + m - 1) // m) * q
    return total_cost


n, p = map(int, input().split())
m, q = map(int, input().split())

result = f(n, p, m, q)
print(result)
