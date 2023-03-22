#面向对象编程--OOP
#一个对象包含了数据和操作数据的函数

#面向过程：
std1={'name':'lisa','score':98}
std2={'name':'bob','score':99}
def print_score(std):
    print(std['name'],':',std['score'])

print_score(std1)

#面向对象
class   Student(object):        #定义类是通过关键词class，类名是Student,类名通常为大写开头的单词。（object）表示该类是从哪里继承下来的，通常，欸有合适的类，就是要object类，这是所有类最终都会继承的类
    def __init__(self,name,score):      #将一些属性强制绑定给class。通过丁一一个特殊的__init__方法，在创建实例的时候把一些属性绑定上去
        self.name=name                  #__init__的第一个参数永远是self，表示创建的实例本身，在创建实例的时候不需要self
        self.score=score
    def print_score(self):              #要定义一个方法（函数），出来第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，出来self不用传递，其他参数正常传入
        print('%s:%s'%(self.name,self.score))
    def get_grade(self):
        if self.score>90:
            print(f'{self.name} is A')
        elif self.score>60:
            print(f'{self.name} is B')
        else:
            print(f'{self.name} is C')
bob=Student('bob',67)
lisa=Student('lisa',78)
bob.print_score()
lisa.print_score()

#面向对象的设计思想是抽出class，根据class创建instance
#面向对象的抽象程度比函数高，因为一个class既包含数据又包含操作数据的方法

#类和实例
print(bob)
#输出<__main__.Student object at 0x000002112B4141C0>    类名和内存地址

class Xkk(object):
    pass
bart=Xkk()
#bart.age=12         #可以自由的给一个实例变量绑定属性
#print(bart.age)


#——数据封装——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#、

lisa.get_grade()

#直接调用实例内部函数，可以不需要知道内部细节
#外部直接通过调用实例变量的函数来操作数据 





#——————————————————访问限制——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

dali=Student('dali',100)
dali.print_score
dali.score=10       #外部代码还是可以只有的修改一个实例的name score属性

#如果要内部属性不被外部访问，可以在属性名称前加上两个下划线_   ,在python中，变量名如果以__开头，就是一个私有变量，只可以内部访问，不能外部访问


class Student1(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print(f'{self.__name}:{self.__score}')
    def get_name(self):         #添加这两个函数，是为了之后可以从外界知道name和score的内容
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):      #为之后在外部修改self.__score提供途径
        self.__score=score

yizheng=Student1('yizheng',100)
#print(yizheng.__name)       #会报错，无法获得内部变量，更不可能从外边修改内部参数
yizheng.__score=100             #不能这么写。这是从外面给yizheng新加了一个__score变量。内部本来的__score已经被python解释器改成了_student_score。所以这样设置的score不是同一个



#—————————继承和多态——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#当我我们定义一个class时，可以从某个现有的class继承，新的class称为子类，而被继承的class被称为基类、父类或超类
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
#对于Dog来说，Animal就是他的父类。对于Animal来说，Dog就是他的子类。Cat和Dog类似
#继承好处：子类获得了父类的全部功能。由于Animal实现了run（）方法。因此dog和cat什么也没有做就自动拥有了run()方法

dog=Dog()
dog.run()

class Dog1(Animal):
    def run(self):
        print('Dog is running')
dog1=Dog1()
dog1.run()              #当子类和父类都存在相同run（）方法时，子类的run()会覆盖父类的run(),在代码运行的时候，总会调用子类的run()————多态

#判断一个变量是否是某个类型，可以用isinstance()判断
print(isinstance(dog,(Animal)))
print(isinstance(dog,(Dog)))        #dog不仅是Dog也是Animal类型

def run_twice(a):
    a.run()
    a.run()

run_twice(dog1)              #函数引用实例不需要到括号       
run_twice(Animal())            #函数应用类需要带括号

class Fff(Animal):
    def run(self):
        print('ssssss')

run_twice(Fff())                #发现只要是animal的子类，就不必对run_twice进行任何修改。由于animal有run()方法，因此只要是该类或者其子类，就会实际调用run()方法

#继承可以把父类的所有功能直接拿来用。子类只需要新增自己特有的方法，也可以把父类不合适的方法覆盖重写

#——————获取对象信息——————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#如何判断对象类型,函数或者其指向的类，使用type()函数
print(type(123),',',type(dog),',',type(abs))
#在if语句判断两个变量的type类型是否相通
import types
if type(123)==int:
    print(1)
if type('abc')==type('1223'):
    print(2)
if type(abs)==types.BuiltinFunctionType:        #判断一个对象是否是函数，可以使用types模块中定义的常量
    print(3)

#对于class的继承关系来说，使用type就很不方便。我们要判断class类型可以使用isinstance（）函数
print(isinstance(dog1,Animal))      #优先使用isintance()判断类型

#————使用dir()——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，他会返回一个包含字符串的list
print(dir('ABX'))
print((len('abc')=='abc'.__len__()))        #len('abc')与'abc'__len__()等价 

class Mydog(object):
    def __len__(self):
        return 100
dog=Mydog()
#调用里面的len函数
print(dog.__len__(),len(dog))   #这两个都是差不多的

#仅仅把属性和方法列出来是不够的，配合"getattr()","setattr()","hasattr()"可以直接操作一个对象的状态

class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=Myobject()
#测试该对象的属性
print(hasattr(obj,'x'))     #有属性'x'吗
setattr(obj,'y',19)         #设置一个属性’y'
print(hasattr(obj,'y'),obj.y,getattr(obj,'y'))  #使用getattr()获取属性‘y'，如果试图获取不存在的属性，会抛出Attributeeror的错误
print(getattr(obj,'z',404))                     #可以在getattr()函数中传入一个default参数，如果属性不存在，就返回默认值404  

#也可以获得对象的方法（函数）
print(hasattr(obj,'power'))  #询问是否有属性“power”
print(getattr(obj,'power'))        #获得属性’power‘
fn=getattr(obj,'power')            #获得属性’power‘并赋值到变量fn,此时fn指向obj.power
print(fn)                              #此时调用fn与调用power是一样的、

#————实例属性和类属性——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Student2(object):
    def __init__(self,name):
        self.name=name
s=Student2('bibi')
s.score=90      #给实例绑定属性的方法有两种：通过实例变量或者通过self变量
print(s.name)

class Student3(object):
    name='stdent'               #stdent2本身需要绑定一个属性，可以直接在class中定义属性，这属于类属性，归stdent类所有
s=Student3()
print(s.name)              #由于实例s没有name属性，所以会继续查找class的name属性
s.name='mybibi'             #给实例绑定name属性
print(s.name)               #由此可以知道实例属性的优先级比class类属性高，因此它会屏蔽类的name属性
print(Student3.name)           #student3的name属性并没有消失，使用student3.name依旧可以访问
del s.name  #删除实例的name属性
print(s.name)   #原本的类属性又重新显示出来了

