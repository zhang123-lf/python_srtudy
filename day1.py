#！/usr/bin/env python3
# -*- coding : utf-8 -*-
#上面两个是为了避免出现中文乱码
a=123#整数
b=False#bool型                   与或非运算：and or not
c='dsda'#字符串
d=None#空值
e=1.1111#float
f=0xff123#16进制数
a=b
b=c
a=12.12
PI=3.1415926#字母大写为常数
print(a/e)#有小数点除法
print(a//e)#整除
s2=r'hello "world"'#r''内部原样输出,\也可以使其原样输出
s3=r'''hello!#多行输出
lisa'''
s1='''和上面的
不一样吗'''
print(s3,s1,s2)
print('中')#python的字符串是以Unicode编写的，支持多种语言
print(ord('A'),ord('中'),chr(20013),chr(24555),'\u4e2d\u6587')#ord和chr为将字符转换为Unicode编码,也可以'\u+对应16进制编码'
x=b'ABC'#bytes类型的数据用带b前缀的单引号或双引号表示
X='ABCD'.encode('ascii')#Unicode表示的str通过encode()方法可以指定编码为指定的bytes
Y='中午'.encode('utf-8')#纯英文可以编码为ASCII码，带中文的编译为utf-8
y=b'ABCP'.decode('ascii')#将bytes类型转为str,需要使用decode（）
num=len(b'ABC')
num1=len('中')#len()是计算str的字符数，换成bytes就是计算字节数
num2=len(b'\xe4\xb8\xad\xe6\x96\x87')#一个中文字符经过UTF-8编码后通常会占用3个字节。而英文字节只占用一个字节
print(num,num1,num2)
print('hello,%s'%'world')#格式化方式与c语言一样，用%实现
print('%d,%2d,%02d,%.3f,%s,%x,%%'%(3,3,3,3.0,'sdds',0xff11441,))#整数和浮点数可以指定是否补零和小数的位数，需要输出%，只需要打两个%即可
print('hello,{0},成绩提升了{1:.1f}%'.format('小明',17.123))#新的格式化字符串方法，他会用传入的参数依次替换字符串内的占位符{0}{1}{2}...
print(f'the area of a circle with radus {a} is {e:.2f}')#{}内的值被对应变量替换



