from sys import stdin, stdout 

x  = int(stdin.readline())

for _ in range(x):
    n = int(stdin.readline())
    t = [int(x) for x in stdin.readline().split()]
    found = False
    first_occurrence = {}
    for i in range(n):
        if t[i] in first_occurrence and i - first_occurrence[t[i]] > 1:
            stdout.write("YES\n")
            found = True
            break
        if t[i] not in first_occurrence:
            first_occurrence[t[i]] = i
    if not found:
        stdout.write("NO\n")