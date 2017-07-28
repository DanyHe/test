#切片 Slice  倒数切片  list或者tuple
#L[:3]      #从0开头可省略
#L[-1]      #去倒数第一个元素
#L[-10:]    #后10个元素
#L[:10:2]   #前10个元素，每两个取一个
#L[::5]     #所有数每5个取一个
#L[:]       #复制一个list



#tuple或者字符串也是特殊的list，在交互性环境：
#>>> (0, 1, 2, 3, 4, 5)[:3]
#(0, 1, 2)
#>>> 'ABCDEFG'[::2]
#'ACEG'



#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）；for..in..:
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items();
#判断一个对象是可迭代对象;
#>>> from collections import Iterable
#>>> isinstance('abc', Iterable) # str是否可迭代
#True


#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。 

#列表生成器 list comprehension  [x * x for x in range(1, 11)]  [x * x for x in range(1, 11)]  [x * x for x in range(1, 11) if x % 2 == 0] >>> [m + n for m in 'ABC' for n in 'XYZ']

#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错

# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 =[s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#一边循环一边计算的机制，称为生成器：generator 方法一： 只要把一个列表生成式的[]改成()，就创建了一个generator；创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator；用next（g）打印一个一个出来；用for循环代替

#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    if n < max:
        print(b)      #要把fib函数变成generator，只需要把print(b)改为yield b
        a,b = b,a+b  #b,a+b相当于一个tuple（b,a+b）
        n = n+1
    return 'done'
#一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator；
#fid函数变成generator;
#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行；
def fid(max):
    n,a,b = 0,0,1
    if n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

#>>>for i in fid(6):
#...   print (i)
        
#for循环调用generator时，发现拿不到generator的return语句的返回值：必须捕获StopIteration错误，返回值包含在StopIteration的value中；

#>>> g = fib(6)
#>>> while True:
#...     try:
#...         x = next(g)
#...         print('g:', x)
#...     except StopIteration as e:
#...         print('Generator return value:', e.value)
#...         break

#杨辉三角

#-*- coding: utf-8 -*-
def triangle1(n):
    L = [1]
    m = 0
    while m <= n:
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0,1)
        L.append(1)
        m = m + 1

        # 期待输出:
        # [1]
        # [1, 1]
        # [1, 2, 1]
        # [1, 3, 3, 1]
        # [1, 4, 6, 4, 1]
        # [1, 5, 10, 10, 5, 1]
        # [1, 6, 15, 20, 15, 6, 1]
        # [1, 7, 21, 35, 35, 21, 7, 1]
        # [1, 8, 28, 56, 70, 56, 28, 8, 1]
        # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles(10):
    print(t)
    n = n + 1
    if n == 10:
        break

#for循环的数据类型有以下：
#1.集合数据类型：list/tuple/dict/set/str等
#2.generator，包括生成器和带yield的generator function

#可以直接作用于for循环的对象统称可迭代对象:Iterable

    
    
