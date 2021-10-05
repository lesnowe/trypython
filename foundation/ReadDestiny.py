import re
with open('命运.txt', 'r', encoding='utf-8') as f:
    prog = re.compile('[\u4e00-\u9fa5]')
    d = {}
    while True:
        c = f.read(1)
        if c == '':
            break 
        if prog.match(c):
            d[c] =d.get(c, 0) + 1
    ls = sorted(d.items(), key=lambda item:item[1], reverse=True) 
    print("{}:{}".format(ls[0][0], ls[0][1]))