x = int(input())
km = 0
for i in range(x):
    a,b = input().split()
    a,b = int(a), int(b)
    km += a*b
print(km)
