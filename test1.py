line = input()

l = 0
r = len(line) - 1

palindrome = 1

while r - l > 1:
    while line[l] == ' ':
        l = l + 1
    while line[r] == ' ':
        r = r - 1
    if r - l > 1:
        if line[l].lower() != line[r].lower():  # No 'A' - 'a' in python
            palindrome = 0
        l = l + 1
        r = r - 1

print(palindrome)
