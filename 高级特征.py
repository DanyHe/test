#��Ƭ Slice  ������Ƭ  list����tuple
#L[:3]      #��0��ͷ��ʡ��
#L[-1]      #ȥ������һ��Ԫ��
#L[-10:]    #��10��Ԫ��
#L[:10:2]   #ǰ10��Ԫ�أ�ÿ����ȡһ��
#L[::5]     #������ÿ5��ȡһ��
#L[:]       #����һ��list



#tuple�����ַ���Ҳ�������list���ڽ����Ի�����
#>>> (0, 1, 2, 3, 4, 5)[:3]
#(0, 1, 2)
#>>> 'ABCDEFG'[::2]
#'ACEG'



#�������һ��list��tuple�����ǿ���ͨ��forѭ�����������list��tuple�����ֱ������ǳ�Ϊ������Iteration����for..in..:
#Ĭ������£�dict��������key�����Ҫ����value��������for value in d.values()�����Ҫͬʱ����key��value��������for k, v in d.items();
#�ж�һ�������ǿɵ�������;
#>>> from collections import Iterable
#>>> isinstance('abc', Iterable) # str�Ƿ�ɵ���
#True


#���Ҫ��listʵ������Java�������±�ѭ����ô�죿Python���õ�enumerate�������԰�һ��list�������-Ԫ�ضԣ������Ϳ�����forѭ����ͬʱ����������Ԫ�ر���
#�κοɵ������󶼿���������forѭ�������������Զ�����������ͣ�ֻҪ���ϵ����������Ϳ���ʹ��forѭ���� 

#�б������� list comprehension  [x * x for x in range(1, 11)]  [x * x for x in range(1, 11)]  [x * x for x in range(1, 11) if x % 2 == 0] >>> [m + n for m in 'ABC' for n in 'XYZ']

#���list�мȰ����ַ������ְ������������ڷ��ַ�������û��lower()�����������б�����ʽ�ᱨ��

# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 =[s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#һ��ѭ��һ�߼���Ļ��ƣ���Ϊ��������generator ����һ�� ֻҪ��һ���б�����ʽ��[]�ĳ�()���ʹ�����һ��generator������L��g�����������������[]��()��L��һ��list����g��һ��generator����next��g����ӡһ��һ����������forѭ������

#쳲���������
def fib(max):
    n,a,b = 0,0,1
    if n < max:
        print(b)      #Ҫ��fib�������generator��ֻ��Ҫ��print(b)��Ϊyield b
        a,b = b,a+b  #b,a+b�൱��һ��tuple��b,a+b��
        n = n+1
    return 'done'
#һ�����������а���yield�ؼ��֣���ô��������Ͳ�����һ����ͨ����������һ��generator��
#fid�������generator;
#generator�ĺ�������ÿ�ε���next()��ʱ��ִ�У�����yield��䷵�أ��ٴ�ִ��ʱ���ϴη��ص�yield��䴦����ִ�У�
def fid(max):
    n,a,b = 0,0,1
    if n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

#>>>for i in fid(6):
#...   print (i)
        
#forѭ������generatorʱ�������ò���generator��return���ķ���ֵ�����벶��StopIteration���󣬷���ֵ������StopIteration��value�У�

#>>> g = fib(6)
#>>> while True:
#...     try:
#...         x = next(g)
#...         print('g:', x)
#...     except StopIteration as e:
#...         print('Generator return value:', e.value)
#...         break

#�������

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

        # �ڴ����:
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

#forѭ�����������������£�
#1.�����������ͣ�list/tuple/dict/set/str��
#2.generator�������������ʹ�yield��generator function

#����ֱ��������forѭ���Ķ���ͳ�ƿɵ�������:Iterable

    
    
