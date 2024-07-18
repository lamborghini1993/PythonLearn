# -*- coding:utf-8 -*-
'''
@Description: 第一个PyOpenGL程序
@Author: lamborghini1993
@Date: 2019-05-23 15:09:11
@UpdateDate: 2019-05-23 20:34:04

犹他茶壶旋转
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)

    # 四方格
    glBegin(GL_LINES)
    glVertex2f(-1, 0)
    glVertex2f(1, 0)
    glVertex2f(0, 1)
    glVertex2f(0, -1)
    glEnd()

    # 右上区域 三个点
    glPointSize(15.0)       # 指明每个点的大小为15个像素，不可以放到glBegin里面
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)    # 指定了绘制的颜色
    glVertex2f(0.3, 0.3)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.6, 0.6)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.9, 0.9)
    glEnd()

    # 左上 正方形 OpenGL在默认情况下，会填充我们画出来的图形
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.2, 0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, 0.2)
    glEnd()

    glColor3f(0.0, 1.0, 1.0)
    
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.8, -0.3)
    glVertex2f(-0.8, -0.6)
    glVertex2f(-0.5, -0.8)
    glVertex2f(-0.2, -0.6)
    glVertex2f(-0.2, -0.3)
    glEnd()
 
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_POLYGON)
    glVertex2f(0.5, -0.1)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.2, -0.6)
    glVertex2f(0.5, -0.8)
    glVertex2f(0.8, -0.6)
    glVertex2f(0.8, -0.3)
    glEnd()
    
    glFlush()


def Init():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Second")
    glutDisplayFunc(drawFunc)
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-1, 1, -1, 1)
    glutMainLoop()


if __name__ == "__main__":
    Init()
