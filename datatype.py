#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#兼容py2除法只能保留整数位问题
from __future__ import division
###################################字符串,upper,lower#########################
#value_l = "this is from string!"
#value_L = "This is From String!"
#新生成的变量为大写，原变量不变
#l_value = value_l.upper()
#新生成的变量为小写，原变量不变
#L_value = value_L.lower()
#print(l_value,L_value)
########验证码样例########
# check_code = 'QWas'
# message = '请输入验证码%s：' %(check_code)
# code = input(message)
# new_check_code = check_code.lower()
# new_code = code.lower()
# if new_code == new_check_code:
#     print('succsess!')
#######################简化版本#######################
# check_code = 'QWas'
# code = input('请输入验证码%s：' %(check_code))
# if code.lower() == check_code.lower():
#     print('success!')
#######################判断是否数字isdigit#######################
# while True:
#     num = input('请输入：')
#     flag = num.isdigit()
#     if flag:
#         num = int(num)
#         break
#     else:
#         print('请输入纯数字!')
#######################去除空格strip#######################
#username = input('your user name: ')   #"     asd      "
#去除右边空格
#new_name = username.rstrip()
#去除左边空格
#final_name = new_name.lstrip()
#去除两边空格
#new_name = username.strip()
#print('--->|',new_name,'|<---')
#######################替换信息replace#######################
# message = '我去123的什么哦,123,woasd123'
# data = message.replace('123','***',2)
# print(data)
#######################切割信息#######################
# message = 'asda,sd1,2asd,casad'
# result1 = message.split(',',1)
# result2 = message.rsplit(',',1)
# print(result1,result2)




