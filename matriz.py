r = 0
T1=[]
T2=[]
T3=[]
T4=[]
T5=[]
T6=[]
while(r!=1):
    aa = input().replace(" ", "")
    a = []
    b=aa.split(')')
    for i in range(len(b)):
        b[i] = b[i]+')'
        if b[i].count('p')>1:
            aux=b[i]
            aux=b[i].split('p')
            for j in range(len(aux)):
                if 'q' in aux[j]:
                    aux[j-1] = aux[j-1] + aux[j]
                    aux.pop(j)
                else:
                    aux[j] = aux[j] + 'p'
            for j in range(len(aux)):
                a.append(aux[j])
        else:
            a.append(b[i])




    for i in range(len(a)):
        if 'Te1p' in a[i]:
            T1.append(a[i])
        if 'Te2p' in a[i]:
            T2.append(a[i])
        if 'Te3p' in a[i]:
            T3.append(a[i])
        if 'Te4p' in a[i]:
            T4.append(a[i])
        if 'Te5p' in a[i]:
            T5.append(a[i])
        if 'Te6p' in a[i]:
            T6.append(a[i])
    print(T1)
    print(T2)
    print(T3)
    print(T4)
    print(T5)
    print(T6)
    T=[T1,T2,T3,T4,T5,T6]
    for i in range(6):
        for j in range(len(T[i])):
            separador = '*Te'+str(i+1)+'p'
            aux=T[i][j].split(separador)
            if (len(aux)> 1):
                T[i][j]=str(round(float(aux[0]),6))+aux[1]
            elif len(aux)==1 and 'q' in aux[0]:
                au = aux[0].replace('Te'+str(i+1)+'p*',"")
                T[i][j]=au
            else:
                aux2=aux[0].replace('Te'+str(i+1)+'p',"")
                if len(aux2)>1:
                    T[i][j]=str(round(float(aux[0])))
                else:
                    T[i][j]='+1'

    if aa == '-1': r=1
    print(T[0])
    print(T[1])
    print(T[2])
    print(T[3])
    print(T[4])
    print(T[5])
    for i in range(6):
        salida ='+'.join(T[i])
        print(salida)