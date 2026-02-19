# import sys

# a = 9 ** 9999
# sys.set_int_max_str_digits(0)
# print(a)

# name = 'aa'
# name1 = 'dd'
# g = 12.5
# age = 23
# info = '我叫%s,我是%s,体重%f,年龄%i' % (name,name1,g,age)

# age = int(input('请输入年龄：'))
# if age <= 10:
#     print('')
# elif age <=18:
#     print('')
# ................

# age = int(input('请输入年龄：'))  或者是写成 18 <= age >= 45
# if age <=45 and age >=18:
#     baogao = input('您是否有体检报告呢？：是/否 ：')
#     if baogao == '是':
#         huiyuandengji = int(input('请输入您的会员等级(1/2/3)：'))
#         if huiyuandengji == 1:
#             print('您的礼品为：纪念体恤')
#         elif huiyuandengji == 2:
#             print('专业跑鞋')
#         elif huiyuandengji == 3:
#             print('运动耳机')
#         else:
#             print('请输入正确数字！！！')
#     else:
#         print('请您先体检！！！')
# else:
#     print('您的年龄不适合参加此次运动  感谢您的参与 ！！！')