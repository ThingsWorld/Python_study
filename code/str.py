#!/usr/bin/python3

str='Runoob'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str[0:-1])           # 输出从第1个开始到倒数第一个的字符
print(str[0:-2])           # 输出从第1个开始到倒数第二个的字符
print(str[0:-3])           # 输出从第1个开始到倒数第三个的字符
print(str[0:-4])           # 输出从第1个开始到倒数第四个的字符
print(str[0:-5])           # 输出从第1个开始到倒数第五个的字符
print(str[0:-6])           # 输出从第1个开始到倒数第六个的字符

#输出:
'''
Runoob
Runoo
R
RunoobRunoob
Runoob你好
noob
Runoo
Runo
Run
Ru
R

'''

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


#输出
"""
------------------------------
hello
runoob
hello\nrunoob
"""
