m, n = map(int, input().split())

digits = []
i = 1
s = ""

while len(digits) < m * n:
    digits += str(i)
    i += 1

for i in range(m):
    for j in range(n):
        s += digits[i * n + j]
    s += '\n'

print(s)
