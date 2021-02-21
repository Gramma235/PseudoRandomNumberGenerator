def PseudoRandomNumberGenerator(seed,NumberLength):
    NumberList=[0]
    flag=True
    while flag==True:
        bufseed=seed**2
        CutLength=int(round((len(str(bufseed))-NumberLength)/2,1))
        seed=int(str(str(bufseed)[CutLength:len(str(bufseed))-CutLength]))
        for i in range(len(NumberList)-1):
            if seed==NumberList[i]:
                flag=False
        else:
            if seed==0:
                flag=False
            else:
                NumberList.append(seed)
                print(seed)
PseudoRandomNumberGenerator(int(input('Введите начальное число: ')),int(input('Введите примерную длину числа на выходе'
                                                                              '(желательно не намного больше длины самого числа): ')))
