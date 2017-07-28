#交互式环境下，输入多行需要换行时，可以
#print（'''line1
#line2
#line3'''）

n = 123
f = 456.789
s1 = 'hello world'
s2 = 'hello.\'Adam\''
s3 = r'hello,"bart"'
s4 = r'''hello,
lisa!'''
print('n = ',n)
print('f = ',f)
print('s1 =\'hello,world\'')
print('s2 = \'hello,\\\'Adam\\\'\'')
print('s3 = r\'hello,\"bart\"\'')
print('s4 = r\'\'\'hello,\nlisa!\'\'\'')

print('''n = 123
f = 456.789
s1 = \'hello world\'
s2 = \'hello.\\\'Adam\\\'\'
s3 = r\'hello,\"bart\"\'
s4 = r\'\'\'hello,
lisa!\'\'\'''')  #两种方式，print（）可以合并打印

#成绩提升百分比，字符串格式显示‘xx.x%’
s1 =72
s2 = 85
r = (s2 -s1)/s1*100
print('提高的百分比为：%.1f %%' % r)#%%用来表示一个%。%d整数,%s字符串,%f浮点数,%x十六进制整数


#list[]   len(list)  list[0],list[1]  list[-1]  list.append()  list.insert()  list.pop()/list.pop(i)  list.
#tuple()  tuple[0],tuple[1]  tuple = (1,)  tuple = (,,[,]) tuple[2][0],tuple[2][1]
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])