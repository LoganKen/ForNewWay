#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
用户三次登陆
1，功能拆分
2，拼凑功能
"""
'''
#功能一：用户登陆
username = input('请输入用户名： ')
password = input('请输入用密码： ')
if username == 'asd' and password == '123'
    print('login usccess!')
else:
    print('login false!')
'''
'''
#功能二：三次机会
#count = 1
#while count <= 3
#    print(count)
#    count += 1
'''
##############功能嵌套#############
#ount = 1
#hile count <= 3:
#   print(count)
#   username = input('请输入用户名： ')
#   password = input('请输入用密码： ')
#   if username == 'asd' and password == '123':
#       print('login usccess!')
#       break
#   else:
#       print('login false!')
#   count += 1
"""
猜年龄游戏，1，最多猜3次。2，三次后还想继续玩回答Y。3，回答N就退出
"""
#最多猜三次
#count = 1
#while count <= 3:
#    username = input('请输入用户名： ')
#    password = input('请输入用密码： ')
#     if username == 'asd' and password == '123':
#         print('login usccess!')
#         break
#     else:
#         print('login false!')
#     if count == 3:
#         choics = input('继续【Y/N】：')
#         if choics == 'Y' or 'y':
#             count = 1
#             continue
#         elif choics == 'N' or 'n':
#             break
#         else:
#             print('choics is worng!')
#             break
#     count += 1
#猜年龄
count = 1
while True:
    age = input('age: ')
    age = int(age)
    if age == 18:
        print('success!')
        break
    else:
        print('wrong!')
    if count == 3:
        choics = input('【Y/N?】: ')
        if choics == 'Y' or 'y':
            count = 1
            continue
        elif choics == 'N' or 'n':
            break
        else:
            break
    timer = 3 - count
    template = '还是输入%s次' %(timer,)
    print(template)
    count += 1