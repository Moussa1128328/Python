def multiply_in_list(x):
    l=[]
    for i in range (1,x+1):
        y=[]
        for j in range (1,i+1):
            y.append(i*j)
        l.append(y)
    return l
