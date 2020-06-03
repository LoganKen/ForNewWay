"""
循环语句
"""
#while True:
count = 0
while count <= 10:
#    if count == 7:
#       pass
 #   else:
#        print(count)
    if count !=7:
        print(count)
    count += 1
"""
break终止当前循环
"""
count = 1
while True:
    print(count)
    count += 1
    if count == 10:
        break
"""
continue不再继续往下走，直接返回while条件
"""
count = 1
while count <= 10:
    if count == 7:
        count += 1
        continue
    print(count)
    count += 1
#不瞒住while后的条件触发，或者=False
else:
    print('this is fron else')
print('ending')
"""
字符串格式化:%s 字符串，%d 数字,打印% 必须使用%%
"""
name = 'Lmaer'
age = 30
template = "%s在闭关，今年%d。" %(name,age,)
print(template)
template = "%s现在手机的电量100%%" %(name,)
print(template)
#运用实例：
name = input('name:')
age = input('age:')
hobby = input('hobby:')
message = """
----------info of Lmaer---------------
Name:  %s
Age:   %s   
hobby: %s      
---------------end--------------------
"""
data = message%(name,age,hobby,)
print(data)
"""
+	加       - 两个对象相加	a + b 输出结果 31
-	减       - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
*	乘       - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
/	除       - x 除以 y	b / a 输出结果 2.1
%	取模     - 返回除法的余数	b % a 输出结果 1
**	幂       - 返回x的y次幂	a**b 为10的21次方
//	取整除    - 向下取接近商的整数
"""
#打印1-100间的奇数
count = 1
while count <= 100:
    num = count % 2
    if num == 1:
        print(count)
    count += 1
#打印1-100间的数相加
total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print(total)
"""
逻辑运算符and，or，not是取反
0,null为false,空格也是有值,true转换位数字位1，false转换数字位0
"""
v1 = 0
v2 = bool(v1)
v3 = ''
v4 = bool(v3)
print(v2)
print(v4)
#第一个值转换成bool,如果是false，取第二个值
#第一个值转换成bool,如果是True，取第第一个值
value = 1 or 9
print(value)
value = 0 or ''
print('--->',value,'<---')
#多个or条件，从左到右依次进行bool运算
value = 0 or False or 8 or 12
print(value)
#and第一个值转换成bool,如果True，取第二个值
#and第一个值转换成bool,如果False，取第一个值
value = 1 and 0
print(value)
#综合先看and再看or,优先级：() > not > and > or
v1 = 1 and 9 or 0 and 5
"""
编码：
ascii
unicode：
        ecs2：2字节
        ecs4：4字节
utf-8：中文用3字节
utf-16
gbk：中文用2字节表示
gb2312：中文用2字节表示
"""











