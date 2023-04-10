# def cacluate(a):
#     b=sum(a)/len(a)
#     l=[]
#     for i in range(len(a)):
#         if a[i]>b:
#             l.append(a[i])
#     return b,l
#
# b0=input("Please input numbers,and press the Enter to end.(gap with ,)\n").split(",")
# b1=list(map(int,b0))
# a=cacluate(b1)
# print(a)

# a=input().split(",")
# sum=1
# for i in a:
#     sum*=int(i)
# print(sum)

# a=input().split()
# b=input()
# c=b.join(a)
# print(c)

# def isprime(n):
#     flag=1
#     for i in range(2,int(pow(n,0.5))+1):
#         if n%i==0:
#             flag=0
#             break
#     if flag==1:
#         return True
#     else:
#         return False
#
# def f(n):
#     l=[]
#     sum=0
#     for i in range(2,n+1):
#         if isprime(i):
#             l.append(i)
#     for a in l[-1:-11:-1]:
#         sum+=a
#     return sum
#
# p=int(input())
# print(f(p))
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# M=eval(input())
# N=eval(input())
# print(gcd(M, N), lcm(M, N))
#

# def y(a,b):
#     temp=0
#     if a>b :
#         while a%b:
#             temp=a
#             a=b
#             b=temp%b
#     elif a<b :
#         temp=a
#         a=b
#         b=temp
#         while a % b:
#             temp = a
#             a = b
#             b = temp % b
#     return b
# def x(a,b):
#     for i in range(1,a*b+1):
#         if i%a==0 and i%b==0:
#             return i
# a=eval(input())
# b=eval(input())
# print(f"{y(a,b)} {x(a,b)}")
import string
# ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']
# l=[]
# i=eval(input())
# if i==1:
#     for a in range(10):
#         l.append(a**3)
#     print(l)
# elif i==2:
#     for a in range(10):
#         if a%2==0:
#             l.append(a**3)
#     print(l)
# elif i==3:
#     for a in range(10):
#         if a%2==1:
#             b=(a,a**3)
#             l.append(b)
#     print(l)
# elif i==4:
#     for a in ls:
#         l.append(a.capitalize())
#     print(l)
# else:
#     print("End of the program")


# ls = ['the lord of the rings', 'anaconda', 'legally blonde', 'gone with the wind']
#
# option = input()
# if option == '1':
#     lst = [i**3 for i in range(10)]
#     print(lst)
# elif option == '2':
#     lst = [i**3 for i in range(0, 10, 2)]
#     print(lst)
# elif option == '3':
#     lst = [(i, i**3) for i in range(10) if i % 2 == 1]
#     print(lst)
# elif option == '4':
#     lst = [s.capitalize() for s in ls]
#     print(lst)
# else:
#     print('End of the program')

import random

# target = 100
# max_num = 1000  # 用户输入的最大值
# min_num = 1  # 用户输入的最小值
# count = 0  # 记录猜的次数
#
# while True:
#     try:
#         guess = int(input())
#         count += 1
#
#         if guess == target:
#             print(f"you have tried {count} times, you win")
#             break
#         elif guess < target:
#             print("less than expected")
#
#         else:
#             print("larger than expected")
#
#     except ValueError:
#         count +=1
#         print("input error")
#         continue

# 猜年龄


for i in list(range(10, 30)):
    i3 = i * i * i
    i4 = i3 * i
    result = 0
    if (i3 >= 1000 and i3 <= 10000) and (i4 >= 100000 and i4 < 1000000):

        sum34 = str(i3) + str(i4)  # '5832'+'104976'
        for j in list(range(0, 10)):
            # 判断0—9字符串在结果字符串的数目，大于1，等于0是错误的
            if sum34.count(str(j)) > 1 or sum34.count(str(j)) == 0:
                result = 0
                break
            elif sum34.count(str(j)) == 1:
                result = i
        # 因为题目要求输出一个整数，即维纳的年龄。所以如果有数符合立即结束循环。
        if (result == i):
            print(result)
            break




