s = "abcdedcba"
n = len(s)//2
mu = len(s)
valid = True
for i in range(n):
    l = s[i]
    r = s[mu-1-i]
    if l != r:
        valid = False
if valid:
    print("yes")
else:
    print("no")
