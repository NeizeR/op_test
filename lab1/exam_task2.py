n = int(input())
m = int(input())

# 3,4 - 3 rows, 4 columns

def num_block(n, m):
    lines = []
    i = 1
    line = ""

    while True:
        s = str(i)
        if len(line + s) > n:
            line += s[:n - len(s)]
            lines.append(line)
            line = s[n - len(s):]
        else:
            line += s
        if len(lines) == m:
            break
        i += 1

    print(lines)
    for i in range(n):
        for j in range(m):
            pass

num_block(n, m)