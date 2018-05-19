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
