def truth_value(seq):
    l=seq
    while len(l)>0:
        if l[0]%2==0:
            l.remove(l[0])
        elif len(l)>1 and l[1]%2!=0:
            l.remove(l[0])
            l.remove(l[0])
        else:
            return 'False'
    return 'True'
    
