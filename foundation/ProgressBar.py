import time as t
print('{:-^30}'.format('执行开始'))
start =  t.perf_counter()
p = 0
s = 1
while True:
    j = t.perf_counter() - start
    print('\r{}%[{:-<50}->]{:.2f}s'.format(p, '*' * s, j), end='')
    if p == 100:
        break
    p += 2
    s += 1
    t.sleep(0.1)
print('\n{:-^30}'.format('执行结束'))