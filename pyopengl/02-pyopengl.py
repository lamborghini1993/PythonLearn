# -*- coding:utf-8 -*-
'''
@Description: 第一个PyOpenGL程序
@Author: lamborghini1993
@Date: 2019-05-23 15:09:11
@UpdateDate: 2019-05-23 17:30:55

犹他茶壶旋转
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.5)

    # glRotatef(1, 0, 1, 0)是一个我们以后会详细讲的函数，简单来说四个参数第一个是角度，后三个是一个向量，意义就是绕着这个向量旋转，这里是绕着Y轴旋转1°。这一度一度的累加，最后使得茶壶围绕Y轴不停的旋转。从这里我们也能看出来，我们指定了一个旋转的角度后，重新绘制并不会复位，而是在上一次旋转的结果上继续旋转。这是一个非常重要的概念，OpenGL是一个状态机，一旦你指定了某种状态，知道再指定位置，它会保持那种状态。不仅仅是旋转，包括以后的光照贴图等等，都遵循这样的规律。
    glRotatef(1, 0, 1, 0)

    glFlush()


def Init():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow("First")
    glutDisplayFunc(drawFunc)

    # glutIdleFunc(Func)又是一个激动人心的函数，可以让OpenGL在闲暇之余，调用一下注册的函数，这是是产生动画的绝好方法。
    glutIdleFunc(drawFunc)

    glutMainLoop()


if __name__ == "__main__":
    Init()
