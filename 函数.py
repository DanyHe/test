#��������ʵ����һ��ָ������������ã���ȫ�����������ı������档
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

#���庯�� def ������������
#�������д������ֵ��return��䷵��
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x
#���뽻��ʽ�����Ѷ���ĵ���python���ɣ�from �ļ��� import ��������ֱ�ӾͿ��Ե��ú����ˣ�

#�պ���def nop������
#            pass  ��Ϊռ�ַ����������ôд����д���뼴��


#�붨��һ������quadratic(a, b, c)������3������������һԪ���η��̣�ax2 + bx + c = 0
#��ʾ������ƽ�������Ե���math.sqrt()������

# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i, (int,float)):
            return '��Ч����'
        if a == 0:
            return'�˷��̷Ƕ�Ԫһ�η��̣�'
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
                return'�˷����޽�'
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
print(quadratic(a, b, c))  

#�����ѭ������a��b��c������Ҫ����һ�ξ�ֻ����֤һ��



#�����Ĳ��� λ�ò���  Ĭ�ϲ���

def power(x,n = 2):
    s = 1
    while n >0:
        n = n-1
        s =s*x
        return s
#power(5) 2�Ϳ���ʡ���ˣ�Ҫ�Ǹĳ����η��ȵȣ���Ҫ�������뼴�ɡ����������ǰ��Ĭ�ϲ����ں�


def enroll(name,gender,age = 6,city = 'Beijing'):
    print('name=:',name)
    print('gender=:',gender)
    print('age=:',sge)
    print('city=:',city)
#Ĭ�ϲ�������Ҫ���룬Ĭ�ϲ���һ����ָ�򲻱����