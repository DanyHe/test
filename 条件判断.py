#if-elif-else
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#318.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖

height =  1.75
weight =83
BMI =weight/(height*height)
if BMI > 32:
    print('严重肥胖')
elif BMI > 28:
    print('肥胖')
elif BMI > 25:
    print('过重')
elif BMI >18.5:
    print('正常')
else:
    print('过轻')
    
#循环
names = ['jack','jones','lily']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum) #print不属于for循环中，若在for循环中，那么打印出每次相加的结果

#while
sum = 0
n =99
while n >0:
    sum =sum +n
    n = n -2
print(sum)  #print不属于while循环，同for类似


L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello,%s!'%x)


#break   提前退出循环
#continue 提前结束本轮循环，直接开始下一轮的循环。这两个语句必须要配合if语句使用


#dict  dictionary ｛‘’*,‘’：*,‘’：* ｝ key-value 拿空间来换时间  dict的key必须是不可变对象。根据key来计算value的存储位置，通过key计算位置的算法为哈希算法（Hash）;
#要避免key不存在的错误，两种：1.‘tom’ in d ture/false  2.d.get('tom',-1) 默认返回none，也可以定义返回-1；
#删除d.pop(key)，对应的value也会从dict中删除；

#set([list]),无须和无重复的集合；重复数据被自动过滤；add（key），可以重复添加，无效；remove（key）；
#set和dict唯一不同的就是set没有存储对应的value。其他都相同；调用对象的自身的任意方法，也不会改变对象本身的内容，只是新建了一个对象返回。