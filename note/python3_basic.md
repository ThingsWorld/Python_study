## 					基础语法

python3 的保留关键字:

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

总共有 33 个,
```

标识符:

```
第一个字符必须是26个字母中的一个,或者下划线 _ ;

除了第一个, 其它的字母,数字,下划线都可以;

对大小写会有区分;
```

注释:

```python
单行注释以 # 开头
多行注释可以多个 #

也可以 
'''
注释 注释 
注释 注释 
'''

或者
"""
注释
注释
"""
```

行与缩进

```python
python 的特色使用缩进表示代码块,不像一些编程语言使用大挂号{}
缩进的空格是可变的,但是同一个代码块必须有着同一样的缩进


例子: line.py
# ! /usr/bin/python3

# 正确的缩进行数
'''
if True:
    print("True")
else:
    print("else")
'''


if True:
    print("True")
  print("True")   # 错误的缩进行数
else:
    print("else")

执行的问题
shiyue@shiyue:~/python3/code$ python3 line.py 
  File "line.py", line 14
    print("True")
                ^
IndentationError: unindent does not match any outer indentation level
shiyue@shiyue:~/python3/code$ 

```

多行语句:

```python
python 一般一行写完一条语句,但是如果语句很长,可以使用反斜杠(\) 实现多行语句
line =  line_one + \
		line_two + \
  		line_three

若是在[] , {}, ()中的多行就不需要 反斜杠(\)
line = ['line_one'
        ,'line_two'
        ,'line_three'
       ]
```

字符串:

- python 中的单引号和双引号使用一模一样.
- 使用三引号('''或""")可以指定一个多行字符串。
- 转义符 '\'
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。


- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
- 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
- Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
- Python中的字符串不能改变。
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
- 字符串的截取的语法格式如下：变量[头下标:尾下标]

```python
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
```

###### 空行:

```
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。
```

###### 同一行显示多条语句

```python
#!/usr/bin/python3

import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```



#### import 与 from...import

在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *