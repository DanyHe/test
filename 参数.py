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
    print('age=:',age)
    print('city=:',city)
#Ĭ�ϲ�������Ҫ���룬��Ҫ�ı�Ĭ�ϲ���ʱ����ʱ�Ϳ��Դ���ʱ���Ըı䣻������˳�򴫲Σ���Ҫ�Ѳ�����Ҳ���ϣ�
#Ĭ�ϲ���һ����ָ�򲻱����
def add_end(L=None):
    if L is None:
        L =[]
    L.append('end') 
    return L
#�ɱ����  ���������ǿɱ��
def calc(numbers):
    sum = 0
    for n in numbers:
        sum =sum+n*n
    return sum
#����ʱ��Ҫһ��list����tuple����calc()
        
def calc(*numbers):
    sum =0
    for n in numbers:
        sum =sum + n*n
    return sum
#�ɱ�����Ѿ���һ��list����tuple�ˣ�ֱ�ӵ��ú������μ�*����calc(*nums)
# *nums��ʾnums���list������Ԫ���ں������ñ�ɲ��������Զ�����һ��tuple��


# **kw�ؼ��ֲ���������0�����߶���������ؼ��ֲ������Զ�����һ��dict�������ǿ�����չ�����Ĺ��ܣ���person('Jack', 24, **extra)
#**extra��ʾ��extra���dict������key-value�ùؼ��ֲ������뵽������**kw������kw�����һ��dict��ע��kw��õ�dict��extra��һ�ݿ�������kw�ĸĶ�����Ӱ�쵽�������extra��


#�����ؼ��ֲ���
def Person(name,age,*,city,job):
    print(name,age,city,job)


#�����������Ѿ�����һ���ɱ������������ſ������ؼ��ֲ����Ͳ���Ҫ*�ˣ�
#�����ؼ��ֲ������봫���������
#���������˳������ǣ���ѡ������Ĭ�ϲ������ɱ�����������ؼ��ֲ����͹ؼ��ֲ�����
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


   # Ĭ�ϲ���һ��Ҫ�ò��ɱ��������ǿɱ���󣬳�������ʱ�����߼�����
   # Ҫע�ⶨ��ɱ�����͹ؼ��ֲ������﷨��
    
   # *args�ǿɱ������args���յ���һ��tuple��
    
   # **kw�ǹؼ��ֲ�����kw���յ���һ��dict��
    
   # �Լ����ú���ʱ��δ���ɱ�����͹ؼ��ֲ������﷨��
    
   # �ɱ�����ȿ���ֱ�Ӵ��룺func(1, 2, 3)���ֿ�������װlist��tuple����ͨ��*args���룺func(*(1, 2, 3))��
    
   # �ؼ��ֲ����ȿ���ֱ�Ӵ��룺func(a=1, b=2)���ֿ�������װdict����ͨ��**kw���룺func(**{'a': 1, 'b': 2})��
    
   # ʹ��*args��**kw��Python��ϰ��д������ȻҲ�����������������������ʹ��ϰ���÷���
    
   # �����Ĺؼ��ֲ�����Ϊ�����Ƶ����߿��Դ���Ĳ�������ͬʱ�����ṩĬ��ֵ��
    
   # ���������Ĺؼ��ֲ�����û�пɱ����������²�Ҫ����д�ָ���*��������Ľ���λ�ò�����
   
# �ݹ麯��
def fact(n):
    if n ==1:
        return 1
    else:
        return n * fact(n-1) #fact(n)��������return n * fact(n - 1)�����˳˷����ʽ�����ԾͲ���β�ݹ���
#β�ݹ��Ż�   β�ݹ���ָ���ں������ص�ʱ�򣬵������������ң�return��䲻�ܰ������ʽ��
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)



# ��ŵ���ƶ�·��
def move(n,a,b,c):
    if n==1:
        print(a+' --> '+c)
    else:
        move(n-1,a,c,b)
        print(a+' --> '+c)
        move(n-1,b,a,c)