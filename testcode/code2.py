for i in range(5):
    for j in range(5):
        if j == 4:
            if i % 2 == 0:
                print(i + 2, end="")
            else:
                print(i + 1, end="")
        else:
            if i % 2 == 0:
                print(i + 1, end="")
            else:
                print(i + 2, end="")
    print()
