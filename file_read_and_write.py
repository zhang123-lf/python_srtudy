f=open('test.txt','r')      #读文件
f.read()                    #文件打开成功，调用read()一次读取文件全部内容
f.close()                   #最后一步调用close（）关闭文件

#如果文件不存在。open（）函数就会抛出IOError的错误，一旦出错后面f.close()就不会调用，所以为了保证
#无论是否出错都能正确关闭文件，可以使用try...finally来实现

try:
    f=open('test.txt','r') 
    print(f.read())
finally:
    if f:
        f.close()
#上面的太过繁琐了，引入with语句来帮我们调用close（）方法：
with open('test.txt','r') as f:
    print(f.read(4))

#read():一次性读完文件全部内容
#read(size):每次最多读取size个字节内容
#readlines():每次读取一行内容，调用readline()一次读取所有内容并按行返回list

with open('test.txt','r') as f:
    print(f.readline(),f.readline())

#二进制文件——————————————————————————————————————————————————————————————————
#前面讲的是读取文本文件，并且是UTF-8编码文件。要读取二进制文件，比如视频图片等等。用‘rb'模式打开文件
f=open('test.jpg','rb')
print(f.read(3),'1')

#字符编码——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#读取非UTF-8编码的文本文件，需要给open（）函数传入encoding参数，例如读取GBK编码文件
#遇到有些编码不规范的文件，会遇到“UnixodeDecodeErrors”，open（）还会接受到一个error参数，最简单的处理方式就是直接忽略
#例子：
#       f=open('gbk.txt','r',encoding='gbk',error='ignore')


#写文件————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
f=open('test.txt','w')  #会将之前文件里原本有的覆盖掉,可以将w换成a,就是在后面继续写入
f.write('你好，世界')
f.close()

with open('test.txt','r') as f:
    print(f.read())

#可以反复调用write()来写入文件，但是一定要用f.close()关闭文件
#只有调用close()方法时，操作系统才保证把没有写入的数据全部写人磁盘
#所以还是用with语句来得保险
with open('test.txt','w') as f:
    f.write('hello world again and again')

with open('test.txt','r') as f:
    print(f.read())