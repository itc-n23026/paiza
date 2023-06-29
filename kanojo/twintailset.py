def f():
    c1, p1 = map(int, input().split())
    c2, p2 = map(int, input().split())

    cp_ratio_1 = c1 / p1
    cp_ratio_2 = c2 / p2

    return 1 if cp_ratio_1 > cp_ratio_2 else 2


output = f()
print(output)
