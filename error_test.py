from functools import reduce

def str2num(s):
    return int(s) if s.find('.')==-1 else float(s)          #句式： 函数/表达式1 if 条件 else 函数/表达式2    满足条件，执行函数/表达式1，不满足执行函数/表达式2

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

import logging
try:
    print('try...')
    main()
except Exception as e:
    print('error:',e)
    logging.exception(e)
else:
    print('no error')
finally:
    print('finally...')
