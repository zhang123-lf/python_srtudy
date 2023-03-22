#!/usr/bin/env python3
#-*- coding: utf-8 -*-
'a test module'
__author__='zhanglf'

#第一行和第二行是标准注释，第一行注释可以让这个.py文件直接在unix/linux/mac上运行，第二行注释表示.py文件本身使用UTF-8编码
#第三行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
#第四行使用_anthor_变量把作者写进去，这样公开源码别人就可以瞻仰你的大名了
#以上是python模块的标准文件模板，后面才是真正代码部分

import sys          #导入模块
def test():
    args=sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello,%s'%args[1])
    else:
        print('too many arguments!')
if __name__=='__main__':        #在命令行运行该模块文件时，python解释器将一个特殊变量__name__置为__main__,如果在其他地方
    test()                      #导入该模块时，if判断将失败，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码

###作用域——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#正常的函数和变量名是公开的（public），可以被直接引用，类似__xxx__这样的变量是特殊变量，可以直接被引用，但是有特殊用途。比如上面的__author__,__name__就是特殊变量，
# 这个模块定义的文档注释也是用__doc__访问，我们自己的变量就不要用这种变量名。
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private）,不应该被直接引用，比如_abc,__abc等                                     


#安装第三方模块



