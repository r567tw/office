# -*- coding: utf-8 -*
#一個驗證是否為身分證字號的py 或者 產生某個數字的身分證字號

import sys,re,string,random

#驗證是否為身分證字號的function,回傳是否驗證成功字串

def verify_id_number(i):
    #將i轉為首字母大寫，其餘字母小寫
    i=i.capitalize()
    if not re.match('^[A-Z][12][0-9]{8}$',i):
        return '此身分證格式不正確,需為0-9,A-Z的字串'
    else:
        a=[]
        a.extend('10987654932210898765431320')
        c=int(a[ord(i[0])-65])+int(i[9])
        for x in range(1,9):
            c+=int(i[x])*(9-x)


        if c%10!=0:
            return '此身分證格式不正確,不通過驗證'
        else:
            return  '此身分證格式正確'

#產生身分證字號

def generate_id_number():
    id_number=(random.choice(string.ascii_letters)).upper()
    a=[]
    a.extend('10987654932210898765431320')
    #求首字母數值
    c=int(a[ord(id_number)-65])
    #性別
    gender=random.randint(1,2)
    c+=gender*8
    id_number+= str(gender)

    #一一相乘
    for x in range(2,9):
        rand_num=random.randint(1,9)
        c+=rand_num*(9-x)
        id_number+= str(rand_num)

    check=c%10
    if (check!=0):
        check=10-check        
    
    id_number+=str(check)

    return id_number
    



if (len(sys.argv)< 2):
    print('請輸入參數\n')
    print('id_number verify [身分證字號]')
    print('id_number random [數字]')
    sys.exit()


parameter=sys.argv[1]
processed=sys.argv[2]


if (parameter== 'verify'):
    result=verify_id_number(processed)
    print(result)    
elif (parameter == 'random'):
    for num in range(0,int(processed)):
        id_number=generate_id_number()
        print(id_number)
        
elif (parameter == '-h'):
    print('id_number verify [身分證字號]')
    print('id_number random [數字]')
else:
    print('ERROR! 請使用 -h')







