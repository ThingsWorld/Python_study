# 			Python3 基本数据类型

###  变量赋值

python 中的变量不需要声明. 每一个变量在使用前必须赋值.

在Python 中,变量就是变量,它没有类型,我们所说的"类型"就是变量所指的内存中对象的类型

等号(=)用来给变量赋值.

等号(=)运算符左边是一个变量名.

```python
#! /usr/bin/python3

integer = 100		# 整型变量
floatvar = 1.2 	# 浮点型变量
name = "hebi"	# 字符串

print(intget)
print(floatvar)
print(name)

# 也可以同时为多个变量赋值
a = b = c = d = e = 1
print(a)
print(b)
print(c)
print(d)
print(e)

# 也可以让三个变量都指向同一个内存,多个对象指定多个变量
q, w, s = 10, 2.3, "hhhh"
print(q)
print(w)
print(s)

# 输出的结果:
shiyue@shiyue:~/python3/Python_study/code/datatype->master$ python3 var.py 
100
1.2
hebi
1
1
1
1
1
10
2.3
hhhh
```

### python3 有六个标准的数据类型:

- Number(数字)

- String(字符串)

- List(列表)

- Tuple(元祖)

- Sets(集合)

- Dictionary(字典)

  不可变数据(四个): Number , String , Tuple, Sets;

  可变数据(两个): List , Dictinoary

  ​

### Number(数字)

python3: int, flaot, bool, complex

```python
# ! /usr/bin/python3
a, b, c, d = 1, 1.1, False, 3+3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 输出的结果:
shiyue@shiyue:~/python3/Python_study/code/datatype->master$ python3 number.py 
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'complex'>
```

isinstance 和 type 的区别在于：

- type()不会认为子类是一种父类类型。
- isinstance()会认为子类是一种父类类型。

### 对象删除:

当你指定一个值时, 一个对象就会被创建, 若是要删除对象,可以使用

```python
integer = 1

print(integer)
# 删除原来的对象
del integer
# 如是再使用, 则会报错 
print(integer)

# 输出结果
shiyue@shiyue:~/python3/Python_study/code/datatype->master$ python3 del.py
1
Traceback (most recent call last):
  File "del.py", line 9, in <module>
    print(Integer)
NameError: name 'Integer' is not defined
```

### 数值运算:

```python
# ! /usr/bin/python3
add = 1 + 1			# 加法
sub = 4 - 2			# 减法
mul = 3 * 2			# 乘法
div_int = 5 / 3     # 除法-----浮点型

# 特殊
div_float = 5 // 3  # 除法-----整型
mul_pow = 3 ** 2    # 乘方

print(add)
print(sub)
print(mul)
print(div_int)

print(div_float)
print(mul_pow)
```

note: 在Python2 中是没有布尔型的, 它是用0 表示False, 1 表示True, Python3 的False和True 值是0和1,

它们也可以和数字进行数值运算

### 字符串

Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。

```Python
# 变量[头下标:尾下标]
# Python 没有单独的字符类型，一个字符就是长度为1的字符串。
>>>word = 'Python'
>>> print(word[0], word[5])
P n
>>> print(word[-1], word[-6])
n P
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
```

note:

- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
- 字符串可以用+运算符连接在一起，用*运算符重复。
- Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
- Python中的字符串不能改变。



### list (列表)

list(列表) 是Python 中使用最频繁的数据类型

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号([])之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

```python
# ! /usr/bin/python3
list = ['he', 111, 3.44, True, 'ii', 22]
list2 = ['shenme', 454]

print(list)
print(list[0])		# 从左往右以0开始, 取第一个值
print(list[1:3])	# 从左往右以0开始, 取第二个值, 从右往左从1开始取值, 倒数第三个
print(list[1:-2])	# 从右往左以-1开始,取第二个值,到倒数第二个
print(list[2:])		# 默认从第三个值到最后
print(list * 2)		# 输出两次列表
print(list + list2) # 链接列表

# 输出的结果:
shiyue@shiyue:~/python3/Python_study/code/datatype->master$ python3 list.py 
['he', 111, 3.44, True, 'ii', 22]
he
[111, 3.44]
[111, 3.44, True]
[3.44, True, 'ii', 22]
['he', 111, 3.44, True, 'ii', 22, 'he', 111, 3.44, True, 'ii', 22]
['he', 111, 3.44, True, 'ii', 22, 'shenme', 454]
```

与Python字符串不一样的是，列表中的元素是可以改变的：

```python
>>>a = [1, 2, 3, 4, 5, 6]
>>> a[0] = 9
>>> a[2:5] = [13, 14, 15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 将对应的元素值设置为 [] 
>>> a
[9, 2, 6]
```

note:

- List写在方括号之间，元素用逗号隔开。
- 和字符串一样，list可以被索引和切片
- List可以使用+操作符进行拼接, 用*运算符重复列表
- List中的元素是可以改变的。

### Tuple (元组)

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

```python
# ! /usr/bin/python3
tuple = ('he', 111, 3.44, True, 'ii', 22)
tuple2 = ('shenme', 454)

print(tuple)
print(tuple[0])		# 从左往右以0开始, 取第一个值
print(tuple[1:3])	# 从左往右以0开始, 取第二个值, 从右往左从1开始取值, 倒数第三个
print(tuple[1:-2])	# 从右往左以-1开始,取第二个值,到倒数第二个
print(tuple[2:])        # 默认从第三个值到最后
print(tuple * 2)        # 输出两次列表
print(tuple + tuple2)   # 链接元组

# 输出的结果:
shiyue@shiyue:~/python3/Python_study/code/datatype->master$ python3 tuple.py 
('he', 111, 3.44, True, 'ii', 22)
he
(111, 3.44)
(111, 3.44, True)
(3.44, True, 'ii', 22)
('he', 111, 3.44, True, 'ii', 22, 'he', 111, 3.44, True, 'ii', 22)
('he', 111, 3.44, True, 'ii', 22, 'shenme', 454)
 
```

note:

可以把字符串看成是一种特殊的元组..它们之间类似



### Set(集合)

集合（set）是一个**无序不重复**元素的序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

```python
#!/usr/bin/python3
 
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
print(b)
 
print(a - b)     # a和b的差集,就是 a 相比b 差什么子集.
print(b - a)  	
 
print(a | b)     # a和b的并集
 
print(a & b)     # a和b的交集
 
print(a ^ b)     # a和b中不同时存在的元素


# 输出的结果:
shiyue@shiyue:~/python3/Python_study/code/datatype->master$ python3 set.py 
{'Jim', 'Tom', 'Mary', 'Rose', 'Jack'}
Rose 在集合中
{'b', 'c', 'd', 'r', 'a'}
{'l', 'c', 'z', 'm', 'a'}
{'b', 'd', 'r'}
{'l', 'm', 'z'}
{'a', 'b', 'd', 'c', 'm', 'r', 'l', 'z'}
{'c', 'a'}
{'b', 'd', 'm', 'r', 'l', 'z'}
```

## Dictionary（字典）

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的**键(key) : 值(value)**对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

```python
#!/usr/bin/python3
 
dict = {}
dict['one'] = "何必"
dict[2]     = "什么"
 
dict2 = {'name': 'heb','code':1, 'site': 'www.hebishi.online'}
 
 
print (dict['one'])     # 输出键为 'one' 的值
print (dict[2])         # 输出键为 2 的值
print (dict2)           # 输出完整的字典
print (dict2.keys())    # 输出所有键
print (dict2.values())  # 输出所有值

# 输出的结果:
shiyue@shiyue:~/python3/Python_study/code/datatype->master$ python3 dict.py 
何必
什么
{'code': 1, 'site': 'www.hebishi.online', 'name': 'heb'}
dict_keys(['code', 'site', 'name'])
dict_values([1, 'www.hebishi.online', 'heb'])

```

note:

- 字典是一种映射类型，它的元素是键值对。
- 字典的关键字必须为不可变类型，且不能重复。
- 创建空字典使用 **{ }**。

## 数据类型转换:

| 函数                      | 描述                              |
| ----------------------- | ------------------------------- |
| int(x [,base])          | 将x转换为一个整数                       |
| float(x)                | 将x转换到一个浮点数                      |
| [complex(real [,imag])] | 创建一个复数                          |
| str(x)                  | 将对象 x 转换为字符串                    |
| repr(x)                 | 将对象 x 转换为表达式字符串                 |
| eval(str)               | 用来计算在字符串中的有效Python表达式,并返回一个对象   |
| tuple(s)                | 将序列 s 转换为一个元组                   |
| list(s)                 | 将序列 s 转换为一个列表                   |
| set(s)                  | 转换为可变集合                         |
| dict(d)                 | 创建一个字典。d 必须是一个序列 (key,value)元组。 |
| frozenset(s)            | 转换为不可变集合                        |
| chr(x)                  | 将一个整数转换为一个字符                    |
| ord(x)                  | 将一个字符转换为它的整数值                   |
| hex(x)                  | 将一个整数转换为一个十六进制字符串               |
| oct(x)                  | 将一个整数转换为一个八进制字符串                |