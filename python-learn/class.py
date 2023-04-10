# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
#
# n = eval(input())
# print("第{}项为：{}".format(n, f(n)))


# def fun(s):
#     flag=1
#     d={}
#     for i in s:
#         if s.count(i)>1:
#             flag=0
#             d[i]=s.count(i)
#     if flag==1:
#         print(s)
#     else:
#         print(d)
# s=input()
# fun(s)

'''斐波那契数列,指得是：1、1、2、3、5、8、13、21、……，
在数学上它得递推公式是：
F(1)=1，
F(2)=1,
F(n)=F(n - 1)+F(n - 2)(n ≥ 3，n ∈ N*)。'''





# #先求出第一个素数，再用n减去这个素数，判断得到的数字是否是素数
# #本题需要调用库函数math.sqrt(),否则会运行超时;
# n = int(input())
# m = [] # 定义一个列表用于存储分解得到的质因数
# while n != 1:
#     for i in range(2, n + 1): # 从最小的2开始尝试
#         while n % i == 0: # 如果有多个相同的质因数就会一直循环
#             m.append(i) # 将因数加入列表之中
#             n /= i
# print(m)

# sum=0
# def kele(n):
#     global sum
#     a,b=divmod(n,3)
#     sum+=a
#     if a+b>=3:
#         kele(a+b)
#     if a+b==2:
#         sum+=1
#     else:
#         return sum
# n=eval(input())
# b=kele(n)
# print(b)


# def triangle(n):
#     l = []
#     for i in range(n):
#         if i == 0:
#             l.append([1])
#         elif i == 1:
#             l.append([1, 1])
#         else:
#             y = []
#             for j in range(i + 1):
#                 if j == 0 or j == i:
#                     y.append(1)
#                 else:
#                     y.append(l[i - 1][j] + l[i - 1][j - 1])
#             l.append(y)
#     return l
#
#
# def printf(n, m):
#     for i in range(n):
#         print(' ' * (block * (n - i)), end='')  # 不换行end=''
#         for j in range(len(x[i])):
#             print(' ' * (block - len(str(x[i][j]))), end='')
#             print(x[i][j], end=' ' * block)
#         print()  # 换行
#
#
# n = int(input())
# x = triangle(n)
# maxNumber = max(x[n - 1])
# block = len(str(maxNumber))
# printf(n, block)



# n = int(input())
# def is_prime(x):
#     flag=1
#     for i in range(2,x):
#         if x%i == 0:
#             flag=0
#             break
#     if flag==1:
#         return 1
#     else:
#         return 0
# if n%2 == 1:
#     print("输入错误")
# for i in range(2,n):
#         if is_prime(i) == 1 and is_prime(n-i) == 1 and i<n-i:
#             print(i,n-i)
#             break



# def rvs(s):
#     if s =="":
#         return s
#     else :
#         return rvs(s[1:])+s[0]
#
# s="abc"
# print(rvs(s))

# op=open('in162.txt','r')
# l=[]
# sum=0.00
# l=op.readline().split()
# print(l)
# for i in l:
#         sum+=eval(i)*0.454
# ip=open('out162.txt','w')
# ip.write("%.2f" %sum)
# op.close()
# ip.close()


# TODO 难啊，好好看
# n = int(input())
# a = []
# b = [0]*n
# for j in range(n):#创建n*n阶矩阵
#     a.append(b[:])
# s = n*n#魔方阵最大的数值
# c = 1#放入数组的值
# x , y = 0 , 0
# while c <= s:
#     for i in range(n):#向右
#         a[y][x] = c
#         c += 1
#         x += 1
#     x -= 1
#     n -= 1#经过第一个for循环之后少掉了一行
#     y += 1
#     for r in range(n):#向下
#         a[y][x] = c
#         c += 1
#         y += 1
#     y -= 1
#     x -= 1#经过第二个循环少掉了一列
#     for l in range(n):#向左
#         a[y][x] = c
#         x -= 1
#         c += 1
#     x += 1
#     n -= 1#经过第三个循环减少了一行
#     y -= 1
#     for k in range(n):#向上
#         a[y][x] = c
#         y -= 1
#         c += 1
#     y += 1
#     x += 1
# with open("file.out", "w") as file:
#     for p in a:
#         for f in p:
#             file.write("%5d"%f)
#         file.write("\n")



def count(t):
    u=l=d=s=others=0
    for i in t:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        elif i.isnumeric():
            d+=1
        elif i.isspace():
            s+=1
        else:
            others+=1
    print(u,l,d,s,others)


def word(fr):
    sum=0
    for line in fr:
        for j in '.'+','+"'":
            line=line.replace(j,'')
        ls=line.split(" ")
        sum+=len(ls)
    return sum
def shiftkey(x):
    sum=0
    for j in x:
        sum+=ord(j)
    return sum

def shift(t,r):
    s=''
    for i in t:
        if i.isupper():
            i=chr(ord('A')+(ord(i)-ord('A')+r)%26)
        elif i.islower():
            i=chr(ord('a')+(ord(i)-ord('a')+r)%26)
        s+=i
    return s

key=shiftkey(input())%26
fr=open("mayun.txt","r")
t=fr.read()#这读完时，指针已经指向了末尾
fr.seek(0)#别再忘了，球球了，因为这个想了半个小时

count(t)
print("{} words in all".format(word(fr)))
print(key)
print(shift(t,key))

fr.close()




