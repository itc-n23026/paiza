def f(M, N):
    result = M - N if M > N else 0
    return result


M, N = map(int, input().split())
output = f(M, N)
print(output)
