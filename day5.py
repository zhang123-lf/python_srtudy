#递归函数
def fact(n):
    if n==1:
        return 1
    else:
       return n*fact(n-1)
#print(fact(1200))           #使用递归1函数要防止栈溢出，递归函数使用次数过多会导致栈溢出

#可以使用尾递归（在函数返回时，调用函数本身，return不含有表达式）的方式防止栈溢出

def fact1(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    else:
        return fact_iter(num-1,num*product)     #符合尾递归

print(fact1(200))

#汉诺塔
def han(n,x,y,z):
    if n==1:
        print(x,'->',z)

    else:
        han(n-1,x,z,y)
        print(x,'->',z)
        han(n-1,y,x,z)
han(2,'x','y','z')

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#切片
L=('me','him','her','your')
print(L[0:1]) #表示从索引0开始去到索引1为止，不包括索引1
print(L[:2])#从零或者-1开始，可以省略
print(L[-2:])
print(L[-3:-1])#倒着取值从倒数第一个取到倒数第三个，不包括倒数第三个
print(L[:4:2])#从零开始，每两个取一个
print(L[::2])#所有数，每两个取一个
print(L[:])#所有数
print(L)

'ABCDEFG'[:2] #字符串也可以看成list,对其进行切片操作

#迭代：如果给一个list或者tuple，可以通过for循环来历遍这个list或tuple——————————————————————————————————————————————————————————————————————————————————————————————
#只要是 可迭代对象。无论有无下标，就都可以迭代
#如何判断一个对象是否时迭代对象，使用collections.abc模块的iterable类型
from collections.abc import Iterable
print(isinstance('abc',Iterable))  #判断str是否可以迭代
d={'a':'1','b':'2','c':'3'}
b=[(1,2),(3,4),(5,6)]
c=('gg',1,2,3,4,5)
def iter(b):
    if not isinstance('b',Iterable):
        print('该数据不可迭代')
    for x,y in b:    #如果输入是成对的数据的话，可以同时引用两个变量
        print(x,y)
iter(b)

for k,v in d.items():               #使用函数.items（）迭代value和key,不加这个只能迭代key
    print(k,'======',v)
#生成类似与java那样的下标循环，可以使用enumerate函数把一个list变成索引-元素对
def iter1(b):
    if not isinstance('b',Iterable):
        print('该数据不可迭代')
    for i,j in enumerate(b):
        print(i,j)
iter1(d)

#列表生成器————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
l=list(range(1,11))#产生1到11的数（不包括11），range()
print(l)

l=[]
for x in range(1,11):
    l.append(x*x)
print(l)
#这个语句可以用下面的简单替代：
L=[x*x for x in range(1,11)]            #写列表生成式时，把要生成的元素x*x放在前面。后面跟着for循环
print(L)
L=[x*x for x in range(1,11) if x%2==0]        #筛选出x被2整除的，在for后面，if后面的是筛选条件，满足的输出，不能加else，否则报错
print(L)
L=[x if x%2==0 else -x for x in range(1,11)]    #***************这种情况必须加else，因为for前面必须加表达式。满足if的条件输出x，不满足输出-x
print(L)
L=[m+n for m in'ABCD' for n in 'abcd']          #双层循环，生成全排列
print(L)
d1=['HELLO','WORLD','FUCK']
L=[k +'='+v for k,v in d.items()]               #k,v必须是str
print(L)
L=[s.lower() for s in d1]                       #lower()函数只对str使用。对list不能用
print(L)
