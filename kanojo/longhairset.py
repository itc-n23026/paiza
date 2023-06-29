def f():
    votes = [input() for _ in range(5)]
    return "yes" if votes.count("yes") > votes.count("no") else "no"


output = f()
print(output)
