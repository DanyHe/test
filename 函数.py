#函数名其实就是一个指向函数对象的引用，完全可以用其他的变量代替。
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

#定义函数 def 函数名（）：
#缩进块编写，返回值用return语句返回
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x
#进入交互式环境把定义的导入python即可：from 文件名 import 函数名，直接就可以调用函数了；

#空函数def nop（）：
#            pass  作为占字符，想好了怎么写，不写代码即可


#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0
#提示：计算平方根可以调用math.sqrt()函数：

# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i, (int,float)):
            return '无效参数'
        if a == 0:
            return'此方程非二元一次方程！'
        else:
            t=b**2-4*a*c
            if t>0:
                x =(-b+math.sqrt(b*b-4*a*c))/(2*a)
                y =(-b-math.sqrt(b*b-4*a*c))/(2*a)
                return x,y
            elif t==0:
                x1,x2=-b/(2*a)
                return x1,x2
            else:
                return'此方程无解'
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
print(quadratic(a, b, c))  

#如何能循环输入a，b，c，不需要运行一次就只能验证一次



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
    print('age=:',sge)
    print('city=:',city)
#默认参数不需要输入，默认参数一定是指向不变对象。