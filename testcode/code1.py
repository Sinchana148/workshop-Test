
def maxStolenval(val):
    preval1 = 0
    preval2 = 0
    for pos in val:
        temp = preval1
        preval1 = max(preval2 + pos, preval1)
        preval2 = temp
    return preval1
val = [6, 7, 1, 3, 8, 2, 5]
print(maxStolenval(val))
