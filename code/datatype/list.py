# ! /usr/bin/python3
list = ['he', 111, 3.44, True, 'ii', 22]
list2 = ['shenme', 454]

print(list)
print(list[0])		# 从左往右以0开始, 取第一个值
print(list[1:3])	# 从左往右以0开始, 取第二个值, 从右往左从1开始取值, 倒数第三个
print(list[1:-2])	# 从右往左以-1开始,取第二个值,到倒数第二个
print(list[2:])		# 默认从第三个值到最后
print(list * 2)		# 输出两次列表
print(list + list2)     # 链接列表

