#函数的参数 位置参数  默认参数

def power(x,n = 2):
    s = 1
    while n >0:
        n = n-1
        s =s*x
        return s
#power(5) 2就可以省略了，要是改成三次方等等，就要重新输入即可。必须参数在前，默认参数在后。


def enroll(name,gender,age = 6,city = 'Beijing'):
    print('name=:',name)
    print('gender=:',gender)
    print('age=:',age)
    print('city=:',city)
#默认参数不需要输入，需要改变默认参数时调用时就可以传参时可以改变；若不按顺序传参，需要把参数名也带上；
#默认参数一定是指向不变对象；
def add_end(L=None):
    if L is None:
        L =[]
    L.append('end') 
    return L
#可变参数  参数个数是可变的
def calc(numbers):
    sum = 0
    for n in numbers:
        sum =sum+n*n
    return sum
#调用时需要一个list或者tuple。如calc()
        
def calc(*numbers):
    sum =0
    for n in numbers:
        sum =sum + n*n
    return sum
#可变参数已经有一个list或者tuple了，直接调用函数传参加*。如calc(*nums)
# *nums表示nums这个list中所有元素在函数调用变成参数传，自动生成一个tuple；


# **kw关键字参数允许传入0个或者多个参数，关键字参数会自动传入一个dict；作用是可以扩展函数的功能；如person('Jack', 24, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


#命名关键字参数
def Person(name,age,*,city,job):
    print(name,age,city,job)


#函数定义中已经有了一个可变参数，后面跟着可命名关键字参数就不需要*了；
#命名关键字参数必须传入参数名；
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


   # 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
   # 要注意定义可变参数和关键字参数的语法：
    
   # *args是可变参数，args接收的是一个tuple；
    
   # **kw是关键字参数，kw接收的是一个dict。
    
   # 以及调用函数时如何传入可变参数和关键字参数的语法：
    
   # 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    
   # 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    
   # 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
    
   # 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
    
   # 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
   
# 递归函数
def fact(n):
    if n ==1:
        return 1
    else:
        return n * fact(n-1) #fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了
#尾递归优化   尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式；
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)



# 汉诺塔移动路线
def move(n,a,b,c):
    if n==1:
        print(a+' --> '+c)
    else:
        move(n-1,a,c,b)
        print(a+' --> '+c)
        move(n-1,b,a,c)