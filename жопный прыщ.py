import webbrowser
print('Задание 1')
print('--------')
print('Из n-ной в 2,8,10')
n=input('Введи число: ')
sum=0
n=n[::-1]
sys=int(input('Введите систему счисления: '))
print('--------')
print('Перевод в 10-ную: ')
for i in range(len(n)):
    a=n[i]
    b=n[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if n.isdigit()==True:
        print(int(n[i]),"* ",sys,'**',i,"=(",(int(n[i])*(sys**i)),") +")
        sum+=int(n[i])*(sys**i)
    elif n.isdigit()==False:
        print(b,'* ',sys,'**',i,'=(',int(a),'*','(',sys,'**',i,')=',int(a)*(sys**i),')',' +')
        sum+=int(a)*(sys**i)
print('Ответ = ',sum,'(10)')
print('--------')

res=sum
ost=''

print('Перевод в 2-ную систему из 10-ной, которая у нас получилась раньше ')
sys_perev=2
c=input('Введи число 2,чтобы перевести: ')

print('--------')
while c!='2':
    print('Неверно введено')
    c=input('Введи число 2,чтобы перевести: ')
print('Действия')
while res>0:
    ost+=str(res%sys_perev)
    print(res,'/ ',sys_perev,'=', res//sys_perev,'(',res%sys_perev,')')
    res//=sys_perev
ost_new=ost[::-1]
print('Ответ: ', ost_new)
print('--------')

res=sum
ost=''


print('Перевод в 8-ную систему из 10-ной, которая у нас получилась раньше')
b=input('Введи число 8,чтобы перевести: ')
print('--------')
sys_perev=8
while b!='8':
    print('Неверно введено')
    b=input('Введи число 8,чтобы перевести: ')    

print('Действия')
while res>0:
    ost+=str(res%sys_perev)
    print(res,'/ ',sys_perev,'=', res//sys_perev,'(',res%sys_perev,')')
    res//=sys_perev
ost_new=ost[::-1]
print('Ответ: ',ost_new)
print('--------')















print('Задание 2')
print('--------')
print('Из рандомной системы в 2,8,10,16')
n=0
ost=''
n=input('Введи число: ')
sum=0
n=n[::-1]
sys=int(input('Введите систему счисления из условия: '))
print('Перевод в 10-ную: ')
for i in range(len(n)):
    a=n[i]
    b=n[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if a=='G' or a=='g' or a=='п' or a=='П':
        a=16
        b='G'
    if a=='H' or a=='h' or a=='р' or a=='Р':
        a=17
        b='H'
    if a=='I' or a=='i' or a=='ш' or a=='Ш':
        a=18
        b='I'
    if a=='J' or a=='j' or a=='о' or a=='О':
        a=19
        b='J'
    if a=='K' or a=='k' or a=='л' or a=='Л':
        a=20
        b='K'
    if a=='L' or a=='l' or a=='д' or a=='Д':
        a=21
        b='L'
    if a=='M' or a=='m' or a=='ь' or a=='Ь':
        a=22
        b='M'
    if a=='N' or a=='n' or a=='т' or a=='Т':
        a=23
        b='N'
    if a=='O' or a=='o' or a=='щ' or a=='Щ':
        a=24
        b='O'
    if a=='P' or a=='p' or a=='з' or a=='З':
        a=25
        b='P'
    if a=='Q' or a=='q' or a=='й' or a=='Й':
        a=26
        b='Q'
    if a=='R' or a=='r' or a=='к' or a=='К':
        a=27
        b='R'
    if a=='S' or a=='s' or a=='ы' or a=='Ы':
        a=28
        b='S'
    if a=='T' or a=='t' or a=='е' or a=='Е':
        a=29
        b='T'
    if a=='U' or a=='u' or a=='г' or a=='Г':
        a=30
        b='U'
    if a=='V' or a=='v' or a=='м' or a=='М':
        a=31
        b='V'
    if a=='W' or a=='w' or a=='ц' or a=='Ц':
        a=32
        b='W'
    if a=='X' or a=='x' or a=='ч' or a=='Ч':
        a=33
        b='X'
    if a=='Y' or a=='y' or a=='н' or a=='Н':
        a=34
        b='Y'
    if a=='Z' or a=='z' or a=='я' or a=='Я':
        a=35
        b='Z'
    if n.isdigit()==True:
        print(int(n[i]),"* ",sys,'**',i,"=(",(int(n[i])*(sys**i)),") +")
        sum+=int(n[i])*(sys**i)
    elif n.isdigit()==False:
        print(b,'* ',sys,'**',i,'=(',int(a),'*','(',sys, '**',i,')=',int(a)*(sys**i),')',' +')
        sum+=int(a)*(sys**i)

print(sum,'(10)')
print('---------')

res=sum
ost=''


print('Перевод в 2-ную систему из 10-ной, которая у нас получилась раньше')
sys_perev=2
c=input('Введи число 2,чтобы перевести: ')
print('--------')
while c!='2':
    print('Неверно введено')
    c=input('Введи число 2,чтобы перевести: ')
print('Действия')
while res>0:
    ost+=str(res%sys_perev)
    print(res,'/ ',sys_perev,'=', res//sys_perev,'(',res%sys_perev,')')
    res//=sys_perev
ost_new=ost[::-1]
print('Ответ: ', ost_new)
print('--------')

res=sum
ost=''


print('Перевод в 8-ную систему из 10-ной, которая у нас получилась раньше')
b=input('Введи число 8,чтобы перевести: ')
print('--------')
sys_perev=8
while b!='8':
    print('Неверно введено')
    b=input('Введи число 8,чтобы перевести: ')    

print('Действия')
while res>0:
    ost+=str(res%sys_perev)
    print(res,'/ ',sys_perev,'=', res//sys_perev,'(',res%sys_perev,')')
    res//=sys_perev
ost_new=ost[::-1]
print('Ответ: ',ost_new)
print('--------')

res=sum
ost=''
print('Перевод в 16-ную систему из 10-ной, которая у нас получилась раньше')
b=input('Введи число 16,чтобы перевести: ')
while b!='16':
    print('Неверно введено')
    b=input('Введи число 16,чтобы перевести: ')
        
print('Действия')
sys=16
ost=''

def num_to_letter(res):
    return(chr(res+55))
while res>0:
    if res%sys>=10:
        ost+=str(num_to_letter(res%sys))
        print(res,'/ ',sys,'=', res//sys,'(',res%sys,'(',num_to_letter(res%sys),') )')
    else:
        ost+=str(res%sys)
        print(res,'/ ',sys,'=', res//sys,'(',res%sys,')')
    res//=sys
ost_new=ost[::-1]
print('Ответ:  ',ost_new)
print('--------')













print('Задание 3')
print('--------')
print('Сложение')

n=input('Введи число: ')
n1=input('Введи 2 число: ')
sum=0
n=n[::-1]
sys=int(input('Введи систему счисления первого слагаемого: '))
sys1=int(input('Введи систему счисления второго слагаемого: '))
print('--------')
#Перевод в 10-ную систему 1 слагаемого
print('Перевод в 10-ную первого слагаемого: ')
for i in range(len(n)):
    a=n[i]
    b=n[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if a=='G' or a=='g' or a=='п' or a=='П':
        a=16
        b='G'
    if a=='H' or a=='h' or a=='р' or a=='Р':
        a=17
        b='H'
    if a=='I' or a=='i' or a=='ш' or a=='Ш':
        a=18
        b='I'
    if a=='J' or a=='j' or a=='о' or a=='О':
        a=19
        b='J'
    if a=='K' or a=='k' or a=='л' or a=='Л':
        a=20
        b='K'
    if a=='L' or a=='l' or a=='д' or a=='Д':
        a=21
        b='L'
    if a=='M' or a=='m' or a=='ь' or a=='Ь':
        a=22
        b='M'
    if a=='N' or a=='n' or a=='т' or a=='Т':
        a=23
        b='N'
    if a=='O' or a=='o' or a=='щ' or a=='Щ':
        a=24
        b='O'
    if a=='P' or a=='p' or a=='з' or a=='З':
        a=25
        b='P'
    if a=='Q' or a=='q' or a=='й' or a=='Й':
        a=26
        b='Q'
    if a=='R' or a=='r' or a=='к' or a=='К':
        a=27
        b='R'
    if a=='S' or a=='s' or a=='ы' or a=='Ы':
        a=28
        b='S'
    if a=='T' or a=='t' or a=='е' or a=='Е':
        a=29
        b='T'
    if a=='U' or a=='u' or a=='г' or a=='Г':
        a=30
        b='U'
    if a=='V' or a=='v' or a=='м' or a=='М':
        a=31
        b='V'
    if a=='W' or a=='w' or a=='ц' or a=='Ц':
        a=32
        b='W'
    if a=='X' or a=='x' or a=='ч' or a=='Ч':
        a=33
        b='X'
    if a=='Y' or a=='y' or a=='н' or a=='Н':
        a=34
        b='Y'
    if a=='Z' or a=='z' or a=='я' or a=='Я':
        a=35
        b='Z'
    if n.isdigit()==True:
        print(int(n[i]),"* ",sys,'**',i,"=(",(int(n[i])*(sys**i)),") +")
        sum+=int(n[i])*(sys**i)
    elif n.isdigit()==False:
        print(b,'* ',sys,'**',i,'=(',int(a),'*','(16**',i,')=',int(a)*(sys**i),')',' +')
        sum+=int(a)*(sys**i)
print(sum,'(10)')
print('--------')


sum1=0
n1=n1[::-1]
print('Перевод в 10-ную второго слагаемого: ')
for i in range(len(n1)):
    a=n1[i]
    b=n1[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if a=='G' or a=='g' or a=='п' or a=='П':
        a=16
        b='G'
    if a=='H' or a=='h' or a=='р' or a=='Р':
        a=17
        b='H'
    if a=='I' or a=='i' or a=='ш' or a=='Ш':
        a=18
        b='I'
    if a=='J' or a=='j' or a=='о' or a=='О':
        a=19
        b='J'
    if a=='K' or a=='k' or a=='л' or a=='Л':
        a=20
        b='K'
    if a=='L' or a=='l' or a=='д' or a=='Д':
        a=21
        b='L'
    if a=='M' or a=='m' or a=='ь' or a=='Ь':
        a=22
        b='M'
    if a=='N' or a=='n' or a=='т' or a=='Т':
        a=23
        b='N'
    if a=='O' or a=='o' or a=='щ' or a=='Щ':
        a=24
        b='O'
    if a=='P' or a=='p' or a=='з' or a=='З':
        a=25
        b='P'
    if a=='Q' or a=='q' or a=='й' or a=='Й':
        a=26
        b='Q'
    if a=='R' or a=='r' or a=='к' or a=='К':
        a=27
        b='R'
    if a=='S' or a=='s' or a=='ы' or a=='Ы':
        a=28
        b='S'
    if a=='T' or a=='t' or a=='е' or a=='Е':
        a=29
        b='T'
    if a=='U' or a=='u' or a=='г' or a=='Г':
        a=30
        b='U'
    if a=='V' or a=='v' or a=='м' or a=='М':
        a=31
        b='V'
    if a=='W' or a=='w' or a=='ц' or a=='Ц':
        a=32
        b='W'
    if a=='X' or a=='x' or a=='ч' or a=='Ч':
        a=33
        b='X'
    if a=='Y' or a=='y' or a=='н' or a=='Н':
        a=34
        b='Y'
    if a=='Z' or a=='z' or a=='я' or a=='Я':
        a=35
        b='Z'
    if n1.isdigit()==True:
        print(int(n1[i]),"* ",sys1,'**',i,"=(",(int(n1[i])*(sys1**i)),") +")
        sum1+=int(n1[i])*(sys1**i)
    elif n1.isdigit()==False:
        print(b,'* ',sys1,'**',i,'=(',int(a),'*','(16**',i,')=',int(a)*(sys1**i),')',' +')
        sum1+=int(a)*(sys1**i)
summ=sum+sum1
print(sum1,'(10)')
print('--------')
print('Теперь просто складываем 2 числа, как обычно потому что мы всегда складываем в десятичной системе: ',sum,'+',sum1,'=',summ)
print('--------')
print('Проверка')
sum=0
if sys==16:
    n=n[::-1]
    b=''

    for i in range(len(n)):
        a=n[i]
        if a=='0':
            a='0000'
        if a=='1':
            a='0001'
        if a=='2':
            a='0010'
        if a=='3':
            a='0011'
        if a=='4':
            a='0100'
        if a=='5':
            a='0101'
        if a=='6':
            a='0110'
        if a=='7':
            a='0111'
        if a=='8':
            a='1000'
        if a=='9':
            a='1001'
        if a=='A' or a=='a' or a=='ф' or a=='Ф':
            a='1010'
        if a=='B' or a=='b' or a=='и' or a=='И':
            a='1011'
        if a=='C' or a=='c' or a=='с' or a=='С':
            a='1100'
        if a=='D' or a=='d' or a=='в' or a=='В':
            a='1101'
        if a=='E' or a=='e' or a=='у' or a=='У':
            a='1110'
        if a=='F' or a=='f' or a=='а' or a=='А':
            a='1111'
        print(n[i],'(',a,')')
        b+=a
    print('Первое число в двоичной: '+b)
    n=str(n)
    f=int(n,16)

elif sys==8:

    sum=0
    n=n[::-1]
    b=''
    for i in range(len(n)):
        a=n[i]
        if a=='0':
            a='000'
        if a=='1':
            a='001'
        if a=='2':
            a='010'
        if a=='3':
            a='011'
        if a=='4':
            a='100'
        if a=='5':
            a='101'
        if a=='6':
            a='110'
        if a=='7':
            a='111'
        print(n[i],'(',a,')')
        b+=a
    print('Первое число в двоичной: '+b)
    n=str(n)
    f=int(n,8)




#условие для 2-го слагаемого


if sys1==16:
    n1=n1[::-1]
    b1=''

    for i in range(len(n1)):
        a=n1[i]
        if a=='0':
            a='0000'
        if a=='1':
            a='0001'
        if a=='2':
            a='0010'
        if a=='3':
            a='0011'
        if a=='4':
            a='0100'
        if a=='5':
            a='0101'
        if a=='6':
            a='0110'
        if a=='7':
            a='0111'
        if a=='8':
            a='1000'
        if a=='9':
            a='1001'
        if a=='A' or a=='a' or a=='ф' or a=='Ф':
            a='1010'
        if a=='B' or a=='b' or a=='и' or a=='И':
            a='1011'
        if a=='C' or a=='c' or a=='с' or a=='С':
            a='1100'
        if a=='D' or a=='d' or a=='в' or a=='В':
            a='1101'
        if a=='E' or a=='e' or a=='у' or a=='У':
            a='1110'
        if a=='F' or a=='f' or a=='а' or a=='А':
            a='1111'
        print(n1[i],'(',a,')')
        b1+=a
    print('Второе число в двоичной: '+b1)
    n1=str(n1)
    q=int(n1,16)

elif sys1==8:

    sum=0
    n1=n1[::-1]
    b1=''
    for i in range(len(n1)):
        a=n1[i]
        if a=='0':
            a='000'
        if a=='1':
            a='001'
        if a=='2':
            a='010'
        if a=='3':
            a='011'
        if a=='4':
            a='100'
        if a=='5':
            a='101'
        if a=='6':
            a='110'
        if a=='7':
            a='111'
        print(n1[i],'(',a,')')
        b1+=a
    n1=str(n1)
    q=int(n1,8)
    print('Второе число в двоичной: '+b1)

g=f+q
print('Сумма чисел в двочной системе: ',bin(g)[2::], '(2)')
a=input('Введите слово open чтобы открыть браузер для того чтобы посмотреть как складывать: ')
if a=='open':
    webbrowser.open_new_tab('https://math.semestr.ru/inf/operation.php')
else:
    print('Написано неверно, перезапустите программу')

print( 'Сумма чисел в 10-ной системе: ',summ, '(10)')
print('----------')

res=summ
ost=''


print('Перевод в 2-ную систему из 10-ной, которая у нас получилась раньше')
sys_perev=2
c=input('Введи число 2,чтобы перевести: ')
print('--------')
while c!='2':
    print('Неверно введено')
    c=input('Введи число 2,чтобы перевести: ')
print('Действия')
while res>0:
    ost+=str(res%sys_perev)
    print(res,'/ ',sys_perev,'=', res//sys_perev,'(',res%sys_perev,')')
    res//=sys_perev
ost_new=ost[::-1]
print('Ответ: ', ost_new)
print('--------')
if int(bin(g)[2::])==int(ost_new):
    print('У нас сошлось то, что мы получили из сложения 10-ной и сложения 2-ной','(',g,'=',ost_new,')')

print('----------')









print('Задание 4')
print('--------')
print('Вычитание')

n=input('Введи число: ')
n1=input('Введи 2 число: ')
vych=0
n=n[::-1]
sys=int(input('Введи систему счисления первого : '))
sys1=int(input('Введи систему счисления второго : '))
print('--------')
#Перевод в 10-ную систему 1 слагаемого
print('Перевод в 10-ную первого : ')
for i in range(len(n)):
    a=n[i]
    b=n[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if a=='G' or a=='g' or a=='п' or a=='П':
        a=16
        b='G'
    if a=='H' or a=='h' or a=='р' or a=='Р':
        a=17
        b='H'
    if a=='I' or a=='i' or a=='ш' or a=='Ш':
        a=18
        b='I'
    if a=='J' or a=='j' or a=='о' or a=='О':
        a=19
        b='J'
    if a=='K' or a=='k' or a=='л' or a=='Л':
        a=20
        b='K'
    if a=='L' or a=='l' or a=='д' or a=='Д':
        a=21
        b='L'
    if a=='M' or a=='m' or a=='ь' or a=='Ь':
        a=22
        b='M'
    if a=='N' or a=='n' or a=='т' or a=='Т':
        a=23
        b='N'
    if a=='O' or a=='o' or a=='щ' or a=='Щ':
        a=24
        b='O'
    if a=='P' or a=='p' or a=='з' or a=='З':
        a=25
        b='P'
    if a=='Q' or a=='q' or a=='й' or a=='Й':
        a=26
        b='Q'
    if a=='R' or a=='r' or a=='к' or a=='К':
        a=27
        b='R'
    if a=='S' or a=='s' or a=='ы' or a=='Ы':
        a=28
        b='S'
    if a=='T' or a=='t' or a=='е' or a=='Е':
        a=29
        b='T'
    if a=='U' or a=='u' or a=='г' or a=='Г':
        a=30
        b='U'
    if a=='V' or a=='v' or a=='м' or a=='М':
        a=31
        b='V'
    if a=='W' or a=='w' or a=='ц' or a=='Ц':
        a=32
        b='W'
    if a=='X' or a=='x' or a=='ч' or a=='Ч':
        a=33
        b='X'
    if a=='Y' or a=='y' or a=='н' or a=='Н':
        a=34
        b='Y'
    if a=='Z' or a=='z' or a=='я' or a=='Я':
        a=35
        b='Z'
    if n.isdigit()==True:
        print(int(n[i]),"* ",sys,'**',i,"=(",(int(n[i])*(sys**i)),") +")
        vych+=int(n[i])*(sys**i)
    elif n.isdigit()==False:
        print(b,'* ',sys,'**',i,'=(',int(a),'*','(16**',i,')=',int(a)*(sys**i),')',' +')
        vych+=int(a)*(sys**i)
print(vych,'(10)')
print('--------')


vych1=0
n1=n1[::-1]
print('Перевод в 10-ную второго : ')
for i in range(len(n1)):
    a=n1[i]
    b=n1[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if a=='G' or a=='g' or a=='п' or a=='П':
        a=16
        b='G'
    if a=='H' or a=='h' or a=='р' or a=='Р':
        a=17
        b='H'
    if a=='I' or a=='i' or a=='ш' or a=='Ш':
        a=18
        b='I'
    if a=='J' or a=='j' or a=='о' or a=='О':
        a=19
        b='J'
    if a=='K' or a=='k' or a=='л' or a=='Л':
        a=20
        b='K'
    if a=='L' or a=='l' or a=='д' or a=='Д':
        a=21
        b='L'
    if a=='M' or a=='m' or a=='ь' or a=='Ь':
        a=22
        b='M'
    if a=='N' or a=='n' or a=='т' or a=='Т':
        a=23
        b='N'
    if a=='O' or a=='o' or a=='щ' or a=='Щ':
        a=24
        b='O'
    if a=='P' or a=='p' or a=='з' or a=='З':
        a=25
        b='P'
    if a=='Q' or a=='q' or a=='й' or a=='Й':
        a=26
        b='Q'
    if a=='R' or a=='r' or a=='к' or a=='К':
        a=27
        b='R'
    if a=='S' or a=='s' or a=='ы' or a=='Ы':
        a=28
        b='S'
    if a=='T' or a=='t' or a=='е' or a=='Е':
        a=29
        b='T'
    if a=='U' or a=='u' or a=='г' or a=='Г':
        a=30
        b='U'
    if a=='V' or a=='v' or a=='м' or a=='М':
        a=31
        b='V'
    if a=='W' or a=='w' or a=='ц' or a=='Ц':
        a=32
        b='W'
    if a=='X' or a=='x' or a=='ч' or a=='Ч':
        a=33
        b='X'
    if a=='Y' or a=='y' or a=='н' or a=='Н':
        a=34
        b='Y'
    if a=='Z' or a=='z' or a=='я' or a=='Я':
        a=35
        b='Z'
    if n1.isdigit()==True:
        print(int(n1[i]),"* ",sys1,'**',i,"=(",(int(n1[i])*(sys1**i)),") +")
        vych1+=int(n1[i])*(sys1**i)
    elif n1.isdigit()==False:
        print(b,'* ',sys1,'**',i,'=(',int(a),'*','(16**',i,')=',int(a)*(sys1**i),')',' +')
        vych1+=int(a)*(sys1**i)
vychd=vych-vych1
print(vych1,'(10)')
print('--------')
print('Теперь просто вычитаем 2 числа, как обычно потому что мы всегда вычитаем в десятичной системе: ',vych,'-',vych1,'=',vychd)
print('--------')
print('Проверка')
sum=0
if sys==16:
    n=n[::-1]
    b=''

    for i in range(len(n)):
        a=n[i]
        if a=='0':
            a='0000'
        if a=='1':
            a='0001'
        if a=='2':
            a='0010'
        if a=='3':
            a='0011'
        if a=='4':
            a='0100'
        if a=='5':
            a='0101'
        if a=='6':
            a='0110'
        if a=='7':
            a='0111'
        if a=='8':
            a='1000'
        if a=='9':
            a='1001'
        if a=='A' or a=='a' or a=='ф' or a=='Ф':
            a='1010'
        if a=='B' or a=='b' or a=='и' or a=='И':
            a='1011'
        if a=='C' or a=='c' or a=='с' or a=='С':
            a='1100'
        if a=='D' or a=='d' or a=='в' or a=='В':
            a='1101'
        if a=='E' or a=='e' or a=='у' or a=='У':
            a='1110'
        if a=='F' or a=='f' or a=='а' or a=='А':
            a='1111'
        print(n[i],'(',a,')')
        b+=a
    print('Первое число в двоичной: '+b)
    n=str(n)
    f=int(n,16)

elif sys==8:

    sum=0
    n=n[::-1]
    b=''
    for i in range(len(n)):
        a=n[i]
        if a=='0':
            a='000'
        if a=='1':
            a='001'
        if a=='2':
            a='010'
        if a=='3':
            a='011'
        if a=='4':
            a='100'
        if a=='5':
            a='101'
        if a=='6':
            a='110'
        if a=='7':
            a='111'
        print(n[i],'(',a,')')
        b+=a
    print('Первое число в двоичной: '+b)
    n=str(n)
    f=int(n,8)




#условие для 2-го слагаемого


if sys1==16:
    n1=n1[::-1]
    b1=''

    for i in range(len(n1)):
        a=n1[i]
        if a=='0':
            a='0000'
        if a=='1':
            a='0001'
        if a=='2':
            a='0010'
        if a=='3':
            a='0011'
        if a=='4':
            a='0100'
        if a=='5':
            a='0101'
        if a=='6':
            a='0110'
        if a=='7':
            a='0111'
        if a=='8':
            a='1000'
        if a=='9':
            a='1001'
        if a=='A' or a=='a' or a=='ф' or a=='Ф':
            a='1010'
        if a=='B' or a=='b' or a=='и' or a=='И':
            a='1011'
        if a=='C' or a=='c' or a=='с' or a=='С':
            a='1100'
        if a=='D' or a=='d' or a=='в' or a=='В':
            a='1101'
        if a=='E' or a=='e' or a=='у' or a=='У':
            a='1110'
        if a=='F' or a=='f' or a=='а' or a=='А':
            a='1111'
        print(n1[i],'(',a,')')
        b1+=a
    print('Второе число в двоичной: '+b1)
    n1=str(n1)
    q=int(n1,16)

elif sys1==8:

    sum=0
    n1=n1[::-1]
    b1=''
    for i in range(len(n1)):
        a=n1[i]
        if a=='0':
            a='000'
        if a=='1':
            a='001'
        if a=='2':
            a='010'
        if a=='3':
            a='011'
        if a=='4':
            a='100'
        if a=='5':
            a='101'
        if a=='6':
            a='110'
        if a=='7':
            a='111'
        print(n1[i],'(',a,')')
        b1+=a
    n1=str(n1)
    q=int(n1,8)
    print('Второе число в двоичной: '+b1)

g=f-q
print('Разность чисел в двочной системе: ',bin(g)[2::], '(2)')
a=input('Введите слово open чтобы открыть браузер для того чтобы посмотреть как вычитать: ')
if a=='open':
    webbrowser.open_new_tab('https://www.calc.ru/dvoichnyy-kalkulyator.html')
else:
    print('Написано неверно, перезапустите программу')

print( 'Разность чисел в 10-ной системе: ',vychd, '(10)')
print('----------')

res=vychd
ost=''


print('Перевод в 2-ную систему из 10-ной, которая у нас получилась раньше')
sys_perev=2
c=input('Введи число 2,чтобы перевести: ')
print('--------')
while c!='2':
    print('Неверно введено')
    c=input('Введи число 2,чтобы перевести: ')
print('Действия')
while res>0:
    ost+=str(res%sys_perev)
    print(res,'/ ',sys_perev,'=', res//sys_perev,'(',res%sys_perev,')')
    res//=sys_perev
ost_new=ost[::-1]
print('Ответ: ', ost_new)
print('--------')
if int(bin(g)[2::])==int(ost_new):
    print('У нас сошлось то, что мы получили из вычитания 10-ной и вычитания 2-ной','(',g,'=',ost_new,')')


print('---------')








print('Задание 5')
print('--------')
print('Умножение')

n=input('Введи число: ')
n1=input('Введи 2 число: ')
umn=0
n=n[::-1]
sys=int(input('Введи систему счисления первого : '))
sys1=int(input('Введи систему счисления второго : '))
print('--------')
#Перевод в 10-ную систему 1 слагаемого
print('Перевод в 10-ную первого : ')
for i in range(len(n)):
    a=n[i]
    b=n[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if a=='G' or a=='g' or a=='п' or a=='П':
        a=16
        b='G'
    if a=='H' or a=='h' or a=='р' or a=='Р':
        a=17
        b='H'
    if a=='I' or a=='i' or a=='ш' or a=='Ш':
        a=18
        b='I'
    if a=='J' or a=='j' or a=='о' or a=='О':
        a=19
        b='J'
    if a=='K' or a=='k' or a=='л' or a=='Л':
        a=20
        b='K'
    if a=='L' or a=='l' or a=='д' or a=='Д':
        a=21
        b='L'
    if a=='M' or a=='m' or a=='ь' or a=='Ь':
        a=22
        b='M'
    if a=='N' or a=='n' or a=='т' or a=='Т':
        a=23
        b='N'
    if a=='O' or a=='o' or a=='щ' or a=='Щ':
        a=24
        b='O'
    if a=='P' or a=='p' or a=='з' or a=='З':
        a=25
        b='P'
    if a=='Q' or a=='q' or a=='й' or a=='Й':
        a=26
        b='Q'
    if a=='R' or a=='r' or a=='к' or a=='К':
        a=27
        b='R'
    if a=='S' or a=='s' or a=='ы' or a=='Ы':
        a=28
        b='S'
    if a=='T' or a=='t' or a=='е' or a=='Е':
        a=29
        b='T'
    if a=='U' or a=='u' or a=='г' or a=='Г':
        a=30
        b='U'
    if a=='V' or a=='v' or a=='м' or a=='М':
        a=31
        b='V'
    if a=='W' or a=='w' or a=='ц' or a=='Ц':
        a=32
        b='W'
    if a=='X' or a=='x' or a=='ч' or a=='Ч':
        a=33
        b='X'
    if a=='Y' or a=='y' or a=='н' or a=='Н':
        a=34
        b='Y'
    if a=='Z' or a=='z' or a=='я' or a=='Я':
        a=35
        b='Z'
    if n.isdigit()==True:
        print(int(n[i]),"* ",sys,'**',i,"=(",(int(n[i])*(sys**i)),") +")
        umn+=int(n[i])*(sys**i)
    elif n.isdigit()==False:
        print(b,'* ',sys,'**',i,'=(',int(a),'*','(16**',i,')=',int(a)*(sys**i),')',' +')
        umn+=int(a)*(sys**i)
print(umn,'(10)')
print('--------')


umn1=0
n1=n1[::-1]
print('Перевод в 10-ную второго : ')
for i in range(len(n1)):
    a=n1[i]
    b=n1[i]
    if a=='A' or a=='a' or a=='ф' or a=='Ф':
        a=10
        b='A'
    if a=='B' or a=='b' or a=='и' or a=='И':
        a=11
        b='B'
    if a=='C' or a=='c' or a=='с' or a=='С':
        a=12
        b='C'
    if a=='D' or a=='d' or a=='в' or a=='В':
        a=13
        b='D'
    if a=='E' or a=='e' or a=='у' or a=='У':
        a=14
        b='E'
    if a=='F' or a=='f' or a=='а' or a=='А':
        a=15
        b='F'
    if a=='G' or a=='g' or a=='п' or a=='П':
        a=16
        b='G'
    if a=='H' or a=='h' or a=='р' or a=='Р':
        a=17
        b='H'
    if a=='I' or a=='i' or a=='ш' or a=='Ш':
        a=18
        b='I'
    if a=='J' or a=='j' or a=='о' or a=='О':
        a=19
        b='J'
    if a=='K' or a=='k' or a=='л' or a=='Л':
        a=20
        b='K'
    if a=='L' or a=='l' or a=='д' or a=='Д':
        a=21
        b='L'
    if a=='M' or a=='m' or a=='ь' or a=='Ь':
        a=22
        b='M'
    if a=='N' or a=='n' or a=='т' or a=='Т':
        a=23
        b='N'
    if a=='O' or a=='o' or a=='щ' or a=='Щ':
        a=24
        b='O'
    if a=='P' or a=='p' or a=='з' or a=='З':
        a=25
        b='P'
    if a=='Q' or a=='q' or a=='й' or a=='Й':
        a=26
        b='Q'
    if a=='R' or a=='r' or a=='к' or a=='К':
        a=27
        b='R'
    if a=='S' or a=='s' or a=='ы' or a=='Ы':
        a=28
        b='S'
    if a=='T' or a=='t' or a=='е' or a=='Е':
        a=29
        b='T'
    if a=='U' or a=='u' or a=='г' or a=='Г':
        a=30
        b='U'
    if a=='V' or a=='v' or a=='м' or a=='М':
        a=31
        b='V'
    if a=='W' or a=='w' or a=='ц' or a=='Ц':
        a=32
        b='W'
    if a=='X' or a=='x' or a=='ч' or a=='Ч':
        a=33
        b='X'
    if a=='Y' or a=='y' or a=='н' or a=='Н':
        a=34
        b='Y'
    if a=='Z' or a=='z' or a=='я' or a=='Я':
        a=35
        b='Z'
    if n1.isdigit()==True:
        print(int(n1[i]),"* ",sys1,'**',i,"=(",(int(n1[i])*(sys1**i)),") +")
        umn1+=int(n1[i])*(sys1**i)
    elif n1.isdigit()==False:
        print(b,'* ',sys1,'**',i,'=(',int(a),'*','(16**',i,')=',int(a)*(sys1**i),')',' +')
        umn1+=int(a)*(sys1**i)
umnd=umn*umn1
print(umn1,'(10)')
print('--------')
print('Теперь просто умнлжим 2 числа, как обычно потому что мы всегда умножаем в десятичной системе: ',umn,'*',umn1,'=',umnd)
print('--------')
print('Проверка')
sum=0
if sys==16:
    n=n[::-1]
    b=''

    for i in range(len(n)):
        a=n[i]
        if a=='0':
            a='0000'
        if a=='1':
            a='0001'
        if a=='2':
            a='0010'
        if a=='3':
            a='0011'
        if a=='4':
            a='0100'
        if a=='5':
            a='0101'
        if a=='6':
            a='0110'
        if a=='7':
            a='0111'
        if a=='8':
            a='1000'
        if a=='9':
            a='1001'
        if a=='A' or a=='a' or a=='ф' or a=='Ф':
            a='1010'
        if a=='B' or a=='b' or a=='и' or a=='И':
            a='1011'
        if a=='C' or a=='c' or a=='с' or a=='С':
            a='1100'
        if a=='D' or a=='d' or a=='в' or a=='В':
            a='1101'
        if a=='E' or a=='e' or a=='у' or a=='У':
            a='1110'
        if a=='F' or a=='f' or a=='а' or a=='А':
            a='1111'
        print(n[i],'(',a,')')
        b+=a
    print('Первое число в двоичной: '+b)
    n=str(n)
    f=int(n,16)

elif sys==8:

    sum=0
    n=n[::-1]
    b=''
    for i in range(len(n)):
        a=n[i]
        if a=='0':
            a='000'
        if a=='1':
            a='001'
        if a=='2':
            a='010'
        if a=='3':
            a='011'
        if a=='4':
            a='100'
        if a=='5':
            a='101'
        if a=='6':
            a='110'
        if a=='7':
            a='111'
        print(n[i],'(',a,')')
        b+=a
    print('Первое число в двоичной: '+b)
    n=str(n)
    f=int(n,8)




#условие для 2-го слагаемого


if sys1==16:
    n1=n1[::-1]
    b1=''

    for i in range(len(n1)):
        a=n1[i]
        if a=='0':
            a='0000'
        if a=='1':
            a='0001'
        if a=='2':
            a='0010'
        if a=='3':
            a='0011'
        if a=='4':
            a='0100'
        if a=='5':
            a='0101'
        if a=='6':
            a='0110'
        if a=='7':
            a='0111'
        if a=='8':
            a='1000'
        if a=='9':
            a='1001'
        if a=='A' or a=='a' or a=='ф' or a=='Ф':
            a='1010'
        if a=='B' or a=='b' or a=='и' or a=='И':
            a='1011'
        if a=='C' or a=='c' or a=='с' or a=='С':
            a='1100'
        if a=='D' or a=='d' or a=='в' or a=='В':
            a='1101'
        if a=='E' or a=='e' or a=='у' or a=='У':
            a='1110'
        if a=='F' or a=='f' or a=='а' or a=='А':
            a='1111'
        print(n1[i],'(',a,')')
        b1+=a
    print('Второе число в двоичной: '+b1)
    n1=str(n1)
    q=int(n1,16)

elif sys1==8:

    sum=0
    n1=n1[::-1]
    b1=''
    for i in range(len(n1)):
        a=n1[i]
        if a=='0':
            a='000'
        if a=='1':
            a='001'
        if a=='2':
            a='010'
        if a=='3':
            a='011'
        if a=='4':
            a='100'
        if a=='5':
            a='101'
        if a=='6':
            a='110'
        if a=='7':
            a='111'
        print(n1[i],'(',a,')')
        b1+=a
    n1=str(n1)
    q=int(n1,8)
    print('Второе число в двоичной: '+b1)

g=f*q
print('Умножение чисел в двочной системе: ',bin(g)[2::], '(2)')
a=input('Введите слово open чтобы открыть браузер для того чтобы посмотреть как умножать: ')
if a=='open':
    webbrowser.open_new_tab('https://math.semestr.ru/inf/multiplication.php')
else:
    print('Написано неверно, перезапустите программу')

print( 'Умножение чисел в 10-ной системе: ',umnd, '(10)')
print('----------')

res=umnd
ost=''


print('Перевод в 2-ную систему из 10-ной, которая у нас получилась раньше')
sys_perev=2
c=input('Введи число 2,чтобы перевести: ')
print('--------')
while c!='2':
    print('Неверно введено')
    c=input('Введи число 2,чтобы перевести: ')
print('Действия')
while res>0:
    ost+=str(res%sys_perev)
    print(res,'/ ',sys_perev,'=', res//sys_perev,'(',res%sys_perev,')')
    res//=sys_perev
ost_new=ost[::-1]
print('Ответ: ', ost_new)
print('--------')
if int(bin(g)[2::])==int(ost_new):
    print('У нас сошлось то, что мы получили из умножения 10-ной и умножения 2-ной','(',g,'=',ost_new,')')
print('-------')
print('Developed by Suntsov Timofey and Danila Chernyavskiy')
print ('Вы понимаете, что надо делать: +79998321679 хахахах')
webbrowser.open_new_tab('online.sberbank.ru/')
