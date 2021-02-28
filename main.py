def PseudoRandomNumberGenerator(seed,NumberLength):
    NumberList=[0]
    flag=True
    while flag==True:
        bufseed=seed**2
        if NumberLength%2!=0 and len(str(bufseed))%2==0 or NumberLength%2==0 and len(str(bufseed))%2!=0:
            bufseed=int('0'+str(bufseed))
        CutLength=int(round((len(str(bufseed))-NumberLength)/2,1))
        seed=int(str(bufseed)[CutLength:len(str(bufseed))-CutLength])
        for i in range(len(NumberList)):
            if seed==NumberList[i]:
                flag=False
        if flag==True:
            print(seed)
            if seed==0:
                flag=False
            else:
                NumberList.append(seed)
PseudoRandomNumberGenerator(int(input('Введите начальное число: ')),int(input('Введите наибольшую длину числа на выходе: ')))
