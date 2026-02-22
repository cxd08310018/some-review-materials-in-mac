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

# a = 1
# b = 2
# c = 0
# while a!=b:
#     print(f'c是{c}')
#     a = int(input('请输入数字B是多少：'))
#     if a == b:
#         print('输入正确，谢谢的您的参与')
#     else:
#         print('输入不正确，请重新输入')

# # 加密文字代码：
# text = input('请输入要加密的文字：')
# se  = ''
# for t in text:
#     se += chr(ord(t) + 1)
# print(f'加密后的文字为：{se}')

# #解密文字代码：
# se = input('请输入要加密的文字：')
# text  = ''
# for s in se:
#     text += chr(ord(s) - 1)
# print(f'加密后的文字为：{text}')

# day = 1
# for day in range(1,31):
#     print(f'**********第{day}天**********')
#     for g in range(1,4):
#         print(f'这是第{g}组仰卧起坐')
#     print(f'第{day}天任务已完成！明天继续 \n')
# print(f'维持 {day}天的运动已结束了，谢谢您！！')

# day = 1
# while day <= 30:
#     print(f'**********第{day}天**********')
#     gr = 1
#     while gr <= 3:
#         print(f'这是第{gr}组仰卧起坐')
#         gr += 1
#     print(f'第{day}天任务已完成！明天继续 \n')
#     day += 1
# print(f'维持 {day - 1}天的运动已结束了，谢谢您！！')

# 乘法表
# for row in range(1,10):
#     for item in range(1,row+1):
#         print(f'{item}*{row}={item*row}',end='\t')
#     print()

# print('欢迎来到挑战赛 输入Q可随时退出 \n')

# qu1,ans1 = 'python用于输出的函数是：','print'
# qu2,ans2 = 'python用于表示逻辑并且的关键字是：','and'
# qu3,ans3 = 'python属于编译形还是解释形：','解释性'

# max_t = 3
# tl = 3
# ip = True

# for le in range(1,tl+1):
#     print(f'******第{le}关******')
#     if le == 1:
#         es1,wer = qu1,ans1
#     elif le == 2:
#         es1,wer = qu2,ans2
#     else:
#         es1,wer = qu3,ans3
#     tr = 1
#     while tr <= max_t:
#         user_input = input(es1)
#         if user_input == wer:
#             print('回答正确\n')
#             break
#         elif user_input == '':
#             print('您的输入为空，请重新作答\n')
#             continue
#         elif user_input == 'Q' or user_input == 'q':
#             print('您已退出游戏\n')
#             ip = False
#             break
#         else:
#             le = max_t - tr
#             if le > 0:
#                 print(f'回答错误，您还剩余{le}机会')
#                 tr += 1
#                 continue
#             else:
#                 print(f'挑战失败 ，本题的正确答案是{wer},游戏结束')
#                 ip = False
#                 break
#     if not ip:
#         break
# if ip:
#     print('恭喜您！全部通过！！')
# 使用递归求阶乘
# def f(num):
#     '''测试自动提示'''
#     if num == 0:
#         return 1
#     else:
#         return num * f( num - 1 )
    
# re = f(5)




def calc_total(*nums):
    '''计算总运动量(个)  nums（元组）可变参数'''
    return sum(nums)

def calc_avg(total,days=7):
    """计算平均值"""
    return total / days

def check_success(total,goal=120):
    '''判定本次挑战是否成功'''
    if total >= goal:
        return '挑战成功！'
    else:
        return '挑战失败！'
    


def main(title,duration,goal):
    print(f'{title}{duration}天挑战赛（请输入每天的数量）')
    num1 = int(input('第一天：'))
    num2 = int(input('第二天：'))
    num3 = int(input('第三天：'))
    #运动总量
    total = calc_total(num1,num2,num3);
    #计算平均值
    avg = calc_avg(total,duration)
    # 判断挑战是否成功
    res = check_success(total,goal)
    print(f'{title}{duration}健身总结')
    # print('总数是：%d,平均值是：%.1f' %(total,avg))
    print(f'总数是：{total},平均值是：{avg:.1f}' )
    print(res)
main('仰卧起坐',3,40)


# def main(title,duration):
#     print(f'{title}{duration}天挑战赛（请输入每天的数量）')
#     num1 = int(input('第一天：'))
#     num2 = int(input('第二天：'))
#     num3 = int(input('第三天：'))
#     num4 = int(input('第四天：'))
#     num5 = int(input('第五天：'))
#     num6 = int(input('第六天：'))
#     num7 = int(input('第七天：'))
#     #运动总量
#     total = calc_total(num1,num2,num3,num4,num5,num6,num7);
#     #计算平均值
#     avg = calc_avg(total)
#     # 判断挑战是否成功
#     res = check_success(total)
#     print(f'{title}{duration}健身总结')
#     # print('总数是：%d,平均值是：%.1f' %(total,avg))
#     print(f'总数是：{total},平均值是：{avg:.1f}' )
#     print(res)
# main('俯卧撑',7)