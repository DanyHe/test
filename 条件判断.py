#if-elif-else
#С�����1.75������80.5kg�������BMI��ʽ�����س�����ߵ�ƽ������С����������BMIָ����������BMIָ����
#����18.5������
#318.5-25������
#25-28������
#28-32������
#����32�����ط���

height =  1.75
weight =83
BMI =weight/(height*height)
if BMI > 32:
    print('���ط���')
elif BMI > 28:
    print('����')
elif BMI > 25:
    print('����')
elif BMI >18.5:
    print('����')
else:
    print('����')
    
#ѭ��
names = ['jack','jones','lily']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum) #print������forѭ���У�����forѭ���У���ô��ӡ��ÿ����ӵĽ��

#while
sum = 0
n =99
while n >0:
    sum =sum +n
    n = n -2
print(sum)  #print������whileѭ����ͬfor����


L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello,%s!'%x)


#break   ��ǰ�˳�ѭ��
#continue ��ǰ��������ѭ����ֱ�ӿ�ʼ��һ�ֵ�ѭ����������������Ҫ���if���ʹ��


#dict  dictionary ������*,������*,������* �� key-value �ÿռ�����ʱ��  dict��key�����ǲ��ɱ���󡣸���key������value�Ĵ洢λ�ã�ͨ��key����λ�õ��㷨Ϊ��ϣ�㷨��Hash��;
#Ҫ����key�����ڵĴ������֣�1.��tom�� in d ture/false  2.d.get('tom',-1) Ĭ�Ϸ���none��Ҳ���Զ��巵��-1��
#ɾ��d.pop(key)����Ӧ��valueҲ���dict��ɾ����

#set([list]),��������ظ��ļ��ϣ��ظ����ݱ��Զ����ˣ�add��key���������ظ���ӣ���Ч��remove��key����
#set��dictΨһ��ͬ�ľ���setû�д洢��Ӧ��value����������ͬ�����ö������������ⷽ����Ҳ����ı����������ݣ�ֻ���½���һ�����󷵻ء�