num = 135
s = str(num)
sum = 0

for pos in range(len(s)):
    sum = sum + int(s[pos]) ** (pos + 1)

print("Sum of digits =", sum)

if sum == num:
    print(num, "is a Disarium number")
else:
    print(num, "is not a Disarium number")


