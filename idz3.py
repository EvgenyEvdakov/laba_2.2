for i in range(10, 1000):
    s = i // 10 + i % 10
    if s + s**2 == i:
        print(i)