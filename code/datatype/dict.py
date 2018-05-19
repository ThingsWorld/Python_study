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
