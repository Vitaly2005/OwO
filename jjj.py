print(''' Есть управление 
ax+b=0
Посмотрим чему равен x при введенных значениях a и b.''')
a = int input('напишите число "a"') 
b = int input('напишите число "b"')
a=int(a)
b=int(b)

if (a==0 and b==0):
    print ('INF')

if (a==0 and b!=0):
    print ('NO')

if (a!=0 and b%a!=0):
    print ('NO') 

if (a!=0 and b%a==0)
    n = int(-b/a) 
    print(n)





