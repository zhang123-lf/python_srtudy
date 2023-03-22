import math
def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        raise TypeError('bad operand type')
    if b*b-4*a*c<0:
        return '方程无解'
    else:
        return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
print(quadratic(1,2,1))

def mul(*a):
    s=1
    if len(a)==0:
        print('请输入内容')
        return 0
    else:
        for x in a:
            s=s*x
        print(f'mul{a}=',s)
mul()

def trim(s):
    x=0
    y=-1
    if not isinstance(s,(str)):
        raise TypeError('参数类型错误：请输入字符串')
    while s[x]=='*':
        x=x+1
    while s[y]=='*':
        y=y-1
    return s[x:len(s)+y+1]
    
print(trim('***zhang**'))

a=[1,2,3,4,5,6]
def findminandmax(L):
    if len(L)==0:           #判断list是否为空list,可以使用len()函数
        return (None,None)
    min=L[0]
    max=L[0]
    for x in L:
        if min>x:
            min=x
        if max<x:
            max=x
    return (min,max)
print(findminandmax(a))

l1=['Hello','World',16,798,'Apple',None]
l2=[x.lower() for x in l1 if isinstance(x,(str))]
print(l2)

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender

bart=Student('bart','man')

print(bart.get_gender())
bart.set_gender('woman')
print(bart.get_gender())


with open('test.txt','r') as f:
    print(f.read())


import re
def is_valid_email(addr):
    re_telephone=re.compile(r'^[a-zA-Z.]+@[a-zA-Z]+\.com$')
    if re_telephone.match(addr):
        print('ok')
    else:
        print('no')

is_valid_email('wceqc.ecmo@gmail.com')
is_valid_email('wceqecmo@gmail.com')
is_valid_email('wceq#mo  gmail.com')

def name_of_email(addr):
    re_name=re.compile(r'^(<?)([a-zA-Z\s]+)(>?)(([a-zA-Z]+)?)(@)([a-zA-Z]+)(\.)(com$)')
    if not re_name.match(addr):
        print('email格式错误')
        return 
    if re_name.match(addr).group(1)=='<'or re_name.match(addr).group(3)=='>':
        if re_name.match(addr).group(1)=='<'and re_name.match(addr).group(3)=='>':
            return re_name.match(addr).group(2)
        else:
            print('email格式错误')
            return 
    else:
        return re_name.match(addr).group(2)
print(name_of_email('wsdaq>whph@wfverkg.com'))

s=['adam','LISA','barT']

def title(s):
    return s.title()
print(list(map(title,s)))
from functools import reduce
def prod(L):
    def ji(x,y):
        return x*y
    return reduce(ji,L)
print(prod([1,3,5,6]))

print(float('1230'))

L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    return t[0]
print(sorted(L,key=by_name))
def by_score(t):
    return t[1]
print(sorted(L,key=by_score))


