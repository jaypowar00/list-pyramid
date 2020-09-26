def pattern(row=None):
    '''
    # usage: pattern( row:int )

    pass integer value (say n) in this funtion to print that n rows of pyramid
    '''
    if row and type(row)==int:
        li = [[' ' if i<(row*2-j)/2 else '*' if i<=(row*2+j)/2 else '\n' for i in range(1,(int((row*2+j)/2)+2))] for j in range(1,row*2,2)]
    else:
        li = [[' ' if i<(8-j)/2 else '*' if i<=(8+j)/2 else '\n' for i in range(1,(int((8+j)/2)+2))] for j in range(1,8,2)]
    a = [i for i in li]
    for i in a:
        for ii in i:
            print(ii,end='')
pattern(6)