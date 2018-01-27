'''
1. 使用函数求前n个数的斐波那契数列。n为函数参数
提示：
 1.斐波那契数列：1,1,2,3,5,8,13,21...即: 起始两项均为1，此后的项分别为前两项之和。
 2.也就是说n=1则返回1，n=2则返回1，n=3则返回2，n=4则返回3，以此类推
'''
# def tt(n):                                       ############迭代
#     n1 = 1
#     n2 = 1
#     n3 = 1
#     if n < 1:
#         print('输入有误！！请输入大于0的数！！')
#         return  -1
#     while (n - 2) > 0:
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return  n3
# a = int(input('请输入一个整数'))
# result = tt(a)
# if result == -1:
#     print('输入有误！！！')
# else:
#     print('第n个数是%s'%result)




#                                                       递归
# def tt(n):
#     if n < 1:
#         print('输入有误！！！')
#         return -1
#     if n == 1 or n == 2:
#         return  1
#     else:
#         return tt(n-1) + tt(n-2)
# a = int(input('请输入一个整数'))
# result = tt(a)
# if result == -1:
#     print('输入有误！！！')
# else:
#     print('第n个数是%s'%result)


def feibo(n):
 a = 1
 b = 1
 i = 1
 while i <= 5:
     if i ==1 or i ==2:
         print(1)
     else:
         a , b = b , a + b
         print(b)
     i += 1

n = int(input("请输入所求数字:"))
feibo(n)
