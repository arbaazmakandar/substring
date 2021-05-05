s = input()
k = set()
for i in range(len(s)):
  for j in range(i, len(s)):
    k.add(s[i:j+1])
print(k)
