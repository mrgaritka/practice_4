k, a, s = map(int, input().split())
if k > a:
    if k >= s:
        print(k)
    else:
        print(s)
elif a > k:
    if a >= s:
        print(a)
    else:
        print(s)
elif s > k:
    if s >= a:
        print(s)
    else:
        print(a)
else:
    print('Ничья')