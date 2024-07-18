# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-06-03 13:29:06
@UpdateDate: 2019-06-03 13:43:44
'''

# 1. 默认位置
print("i {} {}, and I\'am learning".format("like", "python"))

# 2. 设置位置
print("i {1} {0} {1}, and I\'am learning".format("like", "python"))

# 3. 设置关键字
print("i {p} {l}, and I\'am learning".format(l="like", p="python"))

# 4. 元组传参
T = 'like', 'Python'
print('I {0} {1}, and I\'am learning'.format(*T))

# 5. 字典传参
D = {'l': 'like', 'p': 'Python'}
S = 'I {l} {p}, and I\'am learning'.format(**D)
print(S)

# 6. 列表传参
# 定义一个列表
L0 = ['like', 'Python']
L1 = [' ', 'Lerning']
# `[]`前的0、1用于指定传入的列表顺序
S = 'I {0[0]} {1[1]}, and I\'am learning'.format(L0, L1)
print(S)

# 格式限定符
"""
format通过丰富的的“格式限定符”（语法是 {}中带:号)对需要格式的内容完成更加详细的制定。
进制转换
我们可以再限定符中制定不同的字符对数字进行进制转换的格式化，进制对应的表格：
b 二进制
c Unicode 字符
d 十进制整数
o 八进制数
x 十六进制数，a 到 f 小写
X 十六进制数，A 到 F 大写
"""
N = 99
print("{:b}".format(N))
print("{:c}".format(N))
print("{:d}".format(N))
print("{:o}".format(N))
print("{:x}".format(N))
print("{:X}".format(N))

# 填充与对齐
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充，
# 且填充常跟对齐一起使用，^、<、>分别是居中、左对齐、右对齐，后面带宽度。
N = 99
print("{:>8}".format(N))
print("{:<8}".format(N))
print("{:^8}".format(N))
print("{:->8}".format(N))
print("{:-<8}".format(N))
print("{:-^8}".format(N))


# 精度
# :号后面设置精度（以.开始加上精度），然后用f结束，
# 若不是设置，默认为精度为6，自动四舍五入，可带符号显示数字正负标志。
N = 99.1234567
NN = -99.1234567
print('{:f}'.format(N))
print('{:.2f}'.format(N))
print('{:+.2f}'.format(N))
print('{:+.2f}'.format(NN))

# 转义:我们可以使用大括号 {} 来转义大括号
print("i like {}, and {{0}}".format("python"))
