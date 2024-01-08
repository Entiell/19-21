def f(a,b,c,m):
    if a + b + c >= 50: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+2,b,c,m-1), f(a+10,b,c,m-1), f(a+12,b,c,m-1), f(a,b+2,c,m-1), f(a,b+10,c,m-1), f(a,b+12,c,m-1), f(a,b,c+2,m-1), f(a,b,c+10,m-1), f(a,b,c+12,m-1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

#в 19 неудачные ходы у первых двух игроков => разово переписываем all на any

print('19)', [s for s in range(1,19) if f(1, s, s//2, 3)]) #9

print('20)', [s for s in range(1,19) if not f(1, s, s//2, 1) and not f(1, s, s/2, 4)]) #1

print('21)', [s for s in range(1,19) if not f(1, s, s//2, 2) and f(1, s, s//2, 5)]) #5
