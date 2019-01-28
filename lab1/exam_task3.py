f = open("sample.txt")
lines = f.readlines()
f.close()

for i in range(len(lines[0])):
    for j in range(len(lines)):
        print(lines[i][j])