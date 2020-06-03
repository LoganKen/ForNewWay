#-*- coding:utf-8 -*-
#字符串
print('你"好')
print("你'好")
print('''你好''')
print("""这样支持换行，
三双引号，就是这么玩的""")
#整形/数字
print(6666)
print('123123')  #数字以字符串输出
#布尔类型：true/false
print(True)
print(False)
#py2: print "123"
#py3: print("123")
#变量要求：1，名只能包含：字母/数字/下划线。2，数字不能开口。3，不能是Python的关键。
content = '你想输入的字符串'
a3 = 'a3'
_3 = '_3'
#，见名知意
name = 'Lmaer'
age = 30
new_age = age + 1
new_name = name * 2      #python中特殊，复现2两次
print(content,a3,_3,name,age,new_age,new_name)
#布尔类型赋值
value = age >= 19
print(value)
"""
输入输出
"""
#input得到永远是字符串输入，
#py2: name = raw_input("你需要的内容")
#num = input("输入数字：")
#content = 'asd;' + num + name
#print(content)
"""
条件判断
"""
gender = input("请输入性别：")
if gender == "男":
    print('Bye')
elif gender == "女":
    print('come on')
elif gender == "人妖":
    print('go to find Alex')
else:
    print('what are you?')
"""
比较数字
"""
num = input('请输入一个数字：')
#字符串不能直接比较，需要转换成整数型再比较
number = int(num)
if number > 50:
    print('num 大了')
elif number < 50:
    print('num 小了')
"""
比较字符串
"""
name = input('输入用户名：')
password = input('输入密码：')
#if name == '123' and  password == 'asd':
result = name == '123' and  password == 'asd'
if result == True:
    print('login success')
else:
    print('name or password wrong!')
"""
判断嵌套
"""
message = """欢迎致电1000客户
1，查询话费：
2，流程查询：
3，宽带业务：
4，人工服务："""
print(message)
index = input('请选择需要的数字：')
index = int(index)
if index == 1:
    print(1)
elif index == 2:
    print(2)
elif index == 3:
    content = """业务办理
    1，修改密码；
    2，更改套餐；
    3，停机；"""
    print(content)
    value = input('请输入要办理的业务')
    value = int(value)
    if value == 1:
        print(1)
    elif value == 2:
        print(2)
    else:
        print(3)
elif index == 4:
    print(4)
else:
    print('请选择正确数字')