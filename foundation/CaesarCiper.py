'''
请编写一个程序，对输入字符串进行恺撒密码加密，直接输出结果，
其中空格不用进行加密处理。使用input()获得输入。
'''
import re
s = input('请输入一个字符串：')
sp = re.compile('[a-z]')
lp = re.compile('[A-Z]')
for c in s:
    if sp.match(c):
        print(chr(ord('a') + (ord(c) - ord('a') + 3) % 26), end='')
    elif lp.match(c):
        print(chr(ord('A') + (ord(c) - ord('A') + 3) % 26), end='')
    else:
        print(c, end='')