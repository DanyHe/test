#����ʽ�����£����������Ҫ����ʱ������
#print��'''line1
#line2
#line3'''��

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
lisa!\'\'\'''')  #���ַ�ʽ��print�������Ժϲ���ӡ

#�ɼ������ٷֱȣ��ַ�����ʽ��ʾ��xx.x%��
s1 =72
s2 = 85
r = (s2 -s1)/s1*100
print('��ߵİٷֱ�Ϊ��%.1f %%' % r)#%%������ʾһ��%��%d����,%s�ַ���,%f������,%xʮ����������


#list[]   len(list)  list[0],list[1]  list[-1]  list.append()  list.insert()  list.pop()/list.pop(i)  list.
#tuple()  tuple[0],tuple[1]  tuple = (1,)  tuple = (,,[,]) tuple[2][0],tuple[2][1]
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])