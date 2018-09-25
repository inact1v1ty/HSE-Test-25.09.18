line = input()

line = list(line)  # Strings are immutable

n = len(line)

l = 0
r = n - 1

while r - l > 0:
    line[l], line[r] = line[r], line[l]
    l = l + 1
    r = r - 1

substrL = 0
substrR = n - 1
for i in range(n):
    if line[i] == ' ':
        substrR = i - 1
        break

while substrL < n:
    l = substrL
    r = substrR
    while r - l > 0:
        line[l], line[r] = line[r], line[l]
        l = l + 1
        r = r - 1
    substrL = substrR + 2
    if substrL < n:
        substrR = n - 1
        for i in range(substrL, n):
            if line[i] == ' ':
                substrR = i - 1
                break

for i in range(n):
    print(line[i], end='')
print()
