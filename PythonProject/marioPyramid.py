def pyramid(p):
    l=[]
    for i in range(p+1):
        l.append(" ")
    for j in range (0,len(l)):
        l[p-j]="*"
        k=''.join(l)
        print(k)
    return "Complete"