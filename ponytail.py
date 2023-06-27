def f(input_data):
    correct_count = sum(1 for d, e in input_data if d == e)
    return "OK" if correct_count >= 3 else "NG"


input_data = [input().split() for _ in range(5)]
result = f(input_data)
print(result)
