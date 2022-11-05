def convert_string_to_list_of_tuples(S):
    L=[]
    tup=[]
    if len(S)==2:
        return L
    pair=0
    for s in S.split(','):
        x=int(s.replace('[','').replace(']','').replace('(','').replace(')','').replace('\n',''))
        tup+=[x]
        pair+=1
        if pair==2:
            L+=[tuple(tup)]
            pair=0
            tup=[]
    return L
