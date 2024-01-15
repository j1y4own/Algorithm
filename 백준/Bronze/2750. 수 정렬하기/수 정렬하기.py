N = int(input())
l = []
    
for i in range(N):
    n = int(input())
    l.append(n)

l = sorted(set(l))

for i in l:
    print(i)