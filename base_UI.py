import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit,QDesktopWidget #导入pyqt的库

if __name__ == '__main__':#函数的入口
    app = QApplication(sys.argv)#只要是QT制作的app，必须要有且只有一个QApplication对象
                                #sys.argv当作参数的目的是将运行时的命令参数传递给QApplication中
    w = QWidget()#创建一个界面对象

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")
    w.resize(300,200)#设置窗口大小

    #调整窗口在屏幕中心显示
    center_pointer = QDesktopWidget().availableGeometry().center()#获取整个屏幕可用的区域的中央位置
    print(center_pointer)
    x = center_pointer.x()
    y = center_pointer.y()
    # w.move(x, y)
    # w.move(x-150, y-150)
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width // 2, y - height // 2)


    # 在窗口中添加按键
    btn = QPushButton("按钮",w)
    btn.setGeometry(150,120,30,30)#设置位置和大小以左上角为原点

    # 在窗口中添加文本，创建文本时就指定了父对象
    label = QLabel("账号：",w)
    label.setGeometry(10,10,30,30)

    #在窗口中添加输入框
    edit = QLineEdit("请输入账号",w)
    edit.setGeometry(50,10,200,30)


    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
