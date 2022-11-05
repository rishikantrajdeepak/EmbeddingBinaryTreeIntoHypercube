def convert_string_to_list_of_integers(S):
    L=[]
    if len(S)==2:
        return L
    for s in S.split(','):
        x=int(s.replace('[','').replace(']','').replace('\n',''))
        L+=[x]
    return L
