
#python  内置的try...except...finally用来处理错误十分方便，出错时，会分析错误信息并定位错误发生的代码位置才是最关键的,源头一般在最后一行报错！！！！！



try:
    print('try...')
    r=10/0              #怀疑会出错的代码，若是出错直接跳转至错误处理代码，即except语句块，执行完except块后，如果有finally语句块，就执行finally语句块，至此，执行完毕
    print('result:',r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

#若是将检测代码改为’r=10/2‘,如下，由于没有错误发生，except语句块不会被执行，但是finally如果有，就一定会被执行
try:
    print('try...')
    r=10/2              
    print('result:',r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


#不同类型的错误一改由不同的except语句块处理

try:
    print('try...')
    r=10/int('a')              
    print('result:',r)
except ValueError as e:     #捕获错误类型
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error')
finally:
    print('finally...')
print('END')

def foo():
    r=some_function()
    if r==(-1):
        return(-1)
    return r

def bar():
    r=foo()
    if r==(-1):
        print('Error')
    else:
        pass

#python的错误其实是class，所有的错误类型都是继承自basexception,所以在使用except过程中，他不但捕获该类型的错误，还把其子类也一网打尽
try:
    foo()
except NameError as e:
    print('NameError')
except UnboundLocalError as e:   #这个except永远也不会捕获到UnboundLocalError,因为UnboundLocalError是nameError的子类，如果有，那也被第一个except捕获
    print('UnboundLocalError')
finally:
    print('finally')


#使用try...except捕获错误还有个好处。就是可以跨越多层调用，比如函数main()调用bar(),bar()调用fooo(),结果fooo()出错了，这时只要main()捕获到了，就可以处理
def fooo(s):
    return 10/int(s)
def bar(s):
    return fooo(s)*2
def main():
    try:
        bar('s')
    except Exception as e:
        print('error:',e)
    else:
        print('no error')
    finally:
        print('finally...')

main()

#调用栈：
#如果错误没有被捕获，他会一直往上抛，最后被python解释器捕获，打印第一个错误信息，然后程序退出
#出错的时候一定要分析错误的调用栈信息，才能定位错误信息

#记录错误：logging模块——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#如果不捕获错误，自然可以让python解释器来打印出错误栈，但是程序也被结束了。
#既然我们能捕获错误，就可以把错误栈给打印出来，然后分析错误原因，同时，让程序继续执行下去

import logging
def main1():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    
main1()
print('END')

#抛出错误——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#因为错误时class，捕获的一个错误就是捕获到该class的一个实例，错误不是凭空产生的，二十有意创建并抛出的。python的内置函数会抛出很多类型的错误。
#我们自己编写的函数也可以抛出错误

class FooError(ValueError):
    pass

def foo2(s):
    n=int(s)
    if n==0:
        raise FooError('invalue:%s'%s)      #抛出错误
    return 10/n
foo2('1')#*****

#另一种错误处理方法——————————————————————————————————————————————————————————————————————————————
def foo3(s):
    n=int(s)
    if n==0:
        raise ValueError('invalue:%s'%s)      
    return 10/n
def bar():
    try:
        foo3('1')
    except ValueError as e:
        print('valueError')
        raise               #捕获后又将错误抛出,raise语句不带参数，就是会把当卡你错误原样抛出
bar() 

#在except中raise一个error。可以把一种类型的错误转化为另一种类型
try:
    10/0
except ZeroDivisionError:
    raise ValueError('input error')     #理解为捕获这种类型的错误，将另一种错误抛出