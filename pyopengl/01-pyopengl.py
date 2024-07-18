# -*- coding:utf-8 -*-
'''
@Description: 第一个PyOpenGL程序
@Author: lamborghini1993
@Date: 2019-05-23 15:09:11
@UpdateDate: 2019-05-23 17:28:20

https://eyehere.net/2011/learn-opengl-3d-by-pyopengl-3/

OpenGL函数的命名规则
    <前缀><根函数><参数数目><参数类型>
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    # glClear(GL_COLOR_BUFFER_BIT)是把先前的画面给清除，这基本是定律，每次重绘之前都要把原来的画面擦除，否则叠加起来什么都看不出了。glClear一看就知道是OpenGL原生的命令，而参数就是指明要清除的buffer。
    glClear(GL_COLOR_BUFFER_BIT)

    # glutWireTeapot(0.5)是glut提供的绘制犹他茶壶的工具函数
    glutWireTeapot(0.5)

    # glFlush()似乎不用多说，画了那么多，自然要刷新一下显示。不过，这里的刷新不仅仅是屏幕上的更新，实际上，它是处理OpenGL的渲染流水线，让所有排队中的命令得到执行。OpenGL的渲染流水线是一个很重要的概念，不过这里暂时还不打算多说明，否则对初学者来说，未免有些麻烦了。但是这并不意味着可以无视这些基础，知道怎么做只能让你优秀，知道为什么这么做才能让你卓越。
    glFlush()


def Init():
    # glutInit()是用glut来初始化OpenGL的，所有的问题都交给这个函数吧，基本不用管，虽说可以接受参数的，基本无用。
    glutInit()

    # glutInitDisplayMode(MODE)非常重要，这里告诉系统我们需要一个怎样显示模式。至于其参数GLUT_RGBA就是使用(red, green, blue)的颜色系统。有没有写错？这里有个A啊，不应该是(red, green, blue, alpha)么？大概是历史原因，GLUT_RGBA和GLUT_RGB是其实是等价的（坑爹啊），要想实现Alpha还得用其他的参数。而GLUT_SINGLE意味着所有的绘图操作都直接在显示的窗口执行，相对的，我们还有一个双缓冲的窗口，对于动画来说非常合适。
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)

    # glutInitWindowSize(400, 400)这个函数很容易理解，设置出现的窗口的大小。
    # 实际上还有个glutInitWindowPosition()也很常用，用来设置窗口出现的位置。
    glutInitWindowSize(400, 400)

    # glutCreateWindow(“First”)，一旦调用了，就出现一个窗口了，参数就是窗口的标题。
    glutCreateWindow("First")

    # glutDisplayFunc(func)是glut非常讨人喜欢的一个功能，它注册了一个函数，用来绘制OpenGL窗口，这个函数里就写着很多OpenGL的绘图操作等命令，也就是我们主要要学习的东西。
    glutDisplayFunc(drawFunc)

    # glutMainLoop()，主循环，一旦调用了，我们的OpenGL就一直运行下去了。和很多程序中的主循环一样，不停的运行，画出即时的图像，处理输入等。
    glutMainLoop()


if __name__ == "__main__":
    Init()
