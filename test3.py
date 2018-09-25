line = input()
n = int(input())

line = list(line)  # Strings are immutable

for i in range(n):
    for j in range(len(line) - 1, 0, -1):
        line[0], line[j] = line[j], line[0]

for i in range(len(line)):
    print(line[i], end='')
print()
