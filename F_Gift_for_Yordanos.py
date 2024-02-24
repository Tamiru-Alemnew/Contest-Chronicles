wr = input()
alph = [0] * 26

for c in wr:
  alph[ord(c) - ord('a')] += 1

t = []
u = []
i = 0

for c in wr:
  while alph[i] == 0: 
    i += 1
  mn = chr(i + ord('a')) 
  
  while t:
    if t[-1] <= mn:
      u.append(t.pop())
    else:
      break
  
  if c == mn:
    alph[i] -= 1
    u.append(c)
  else:
    alph[ord(c) - ord('a')] -= 1
    t.append(c)

while len(t) > 0:
  u.append(t.pop())

print("".join(u))