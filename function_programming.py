#函数式编程的特点就是：允许把函数本身作为参数传入另一个函数，还允许返回另一个函数
print(abs(-190),'\n',abs)   #abs(-190)是函数调用，abs就是函数本身
a=abs(-10)
f=abs
print(a,f)
#结论：函数本身也是可以赋值给变量，即变量可以指向函数

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接受另一个函数作为参数，这种函数就是高阶函数

#一个最简单的高阶函数：
def add(x,y,f):
    return f(x)+f(y)
print(add(10.2,-10,abs))

#编写高阶函数，就是让函数的参数能够接收别的函数

#高阶函数————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#python内建了map（）和reduce（）函数
#map()函数接收两个参数，一个是函数，一个是Iterable(可迭代)，map将传入的函数依次作用到序列的每个元素中，并把新结果作为新的Iterator
r=map(abs,[0,-1,-2,-3,-45])
print(list(r))  #map（）函数返回的值为Iterator（惰性序列），需要通过list()函数让它把整个序列计算出来并返回一个list
#上述代码效果与下面的一致：
L=[]
for n in [-1,-2,-3,-45]:
    L.append(f(n))
print(L)

#更简洁的写法：
print(list(map(str,[1,2,3,4,5])))

#reduce()函数的用法：
#reduce把一个函数作用在一个序列[x0,x1,x2,x3,...]上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素做积累计算
#其效果就是：reduce(f,[x0,x1,x2,x3....])=f(f(f(f(x0,x2),x2),x3),x4)
from functools import reduce
def add1(x,y):
    return x+y 
print(reduce(add1,[1,2,3,4,5]))

def char2num(s):
    if isinstance(s,str):
        dights={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9 ,'0':0}
    return dights[s]
print(list(map(char2num,'12313')))#整数不可迭代，map()返回的是个惰性序列，压频用list转化一下

#filter（）——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#和map()类似，fiter()也接收一个函数和序列。和map不同的是，fiter()把传入的函数依次作用于每个元素，然后根据返回值是ture还是false决定保留还是丢弃该元素
def is_odd(n):
    return n%2==1
print('标记',list(filter(is_odd,[1,2,3,4,5,6,7,8,9,0])))

def not_empty(s):
    return s and s.strip()#strip()函数删除空格
print(list(filter(not_empty,[' fe ',' ','wrfv ',None,'   '])))


#sorted——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
print(sorted([132,34,6,4,78,679,-1]))#排序，比大小

print(sorted([-132,-4,6,-4,78,-69,-1],key=abs))#通过接受一个key函数来实现自定义排序，比如这个按绝对值排序

print(sorted(['see','Gaw','we','aA','SR','FH']))
print(sorted(['sEE','Gaw','we','aA','SR','FH'],key=str.lower))#原本排序他会按照ASCII码大小比较，加上这个key函数，就是取消大小写了
print(sorted(['sEE','Gaw','we','aA','SR','FH'],key=str.lower,reverse=True))#将之前的结果反向排序

