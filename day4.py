#调用函数，函数在官网有

#数据类型转化： int('123') 就是将字符串转换为整数

#还可以将函数头给一个变量,通过这个变量来调用函数：
a=abs
print(a(-9))

#定义函数
def my_abs1(x):
    if not isinstance(x,(int,float)):               #如果是输入参数的个数不对，python会自己检查出来
        raise TypeError('bad opeerand type')        #如果是参数类型不对，就无法检查。参数类型可以通过 isinstance() 实现，只允许整数和浮点数
    if x>=0:
        return x
    else:
        return -x
    

from my_function import my_abs     #导入其他文件定义的函数

print(my_abs1(-20))

#返回多个值：

import math                    #表示导入math包，方便之后引用里面的函数sin,cos等

def move(x,y,step,angle=0.0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
x,y=move(0,0,10,math.pi/3)      #python函数返回的仍然是单一值，类型为tuple，只是逐一赋值给x,y
print(x)
r=move(0,0,60,math.pi/6) 
print(r)

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#

#函数的参数

def power(x,n=2):       #设置了一个默认参数，只需要输入一个参数就行了
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(3,3))
print('power',power(3))

def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll(gender='zhao',name='m',city='shanghai')      #可以不按照顺序输入参数，但是要带上参数名

#定义默认参数必须指向不可变对象！！！！！

def def_end(L=None):        #要是L=[]（空list,一个可变对象）多次调用该函数结果是不一样的
    if L is None:
        L=[]
    L.append('END')
    return L


#可变参数——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

def calc(number):       #此时number可以输入一个tuple或者list，调用的时候需要先组装一个list或者tuple，比如calc（[1,2,3,4]）
    sum=0
    for x in number:
        sum=sum+x
    return sum

def calc1(*number):     #将number改为可变参数，可以直接输入一串数字或者不输入，比如 calc1（1，2，3，4）。在输入为一个tuple或者list时，可以在调用的时候加个*，把其元素变为可变参数传进去
    sum=0               
    for x in number:
        sum=sum+x
    return sum

nums=[1,2,3,4]

print(calc(nums),calc1(*nums),calc1(1,2,3,4),calc1())       #例子

#关键字参数——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#可变参数允许传入任意个或者0个参数
#关键字参数允许传入任意或者0个含参数名的参数

def person(name,age,**kw):              
    print('name:',name,'age:',age,kw)
person('bob',7)
person('bob',7,city='beijing')
extra={'city':'beijing','job':'teacher','love':'woman'}
person('lili',5,city=extra['city'])         #关键字参数可以和dict联用，只需要加上**就可以将extra这个dict的所有key-value用关键字参数传入函数的**kw参数
person('lisa',5,**extra)                    #kw获得的时extra的一份拷贝，对kw的改动不会影响函数外的extra

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#命名关键字参数

def person1(name,age,*,city,job):       #与关键字**wk不同,命名关键字参数需要一个特殊的分隔符'*',*字后面的被视为命名关键字
    print(name,age,city,job)

person1('bob',9,city=10,job=110)

def person2(name,age,*arg,city,job):   #要是函数定义中有个可变函数，之后跟着的命名关键字就不用*分隔符了
    print(name,age,arg,city,job)
person2('zhao',7,2,3,4,city='shanghai',job=110)

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#参数组合
def fi(a,b,c=0,*arg,**kw):
    print(a,b,c,arg,kw)
def fi1(a,b,c=0,*,d,**kw):
    print(a,b,c,d,kw)

fi(1,2,*nums,city=10)
fi1(1,2,d=3,s=12,**extra)

#任何函数都可以通过类似的functon(*arg,**extra)