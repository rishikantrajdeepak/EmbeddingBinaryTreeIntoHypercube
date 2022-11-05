#input S is the sequence of 1 caterpillar (first leg), whose at most three vertices are to be fixed. returns fixed three vertices along with parity

def fix_vertices(S):
    Fix=[] #tuples of fixed vertices
    Parity=[] #tuples of parity of fixed vertices
    parity=[1] #parity of fixed vertices w.r.t. to each other, first vertex is given +1 parity
    fix=[0] #first backbone is always chose
    s=1
    for i in range(1,len(S)):
        if S[i]>1:
            fix+=[s,s+S[i]-1]
            if i%2==0:
                parity+=[1]
            else:
                parity+=[-1]
            if (S[i]-1)%2==0:
                parity.append(parity[1])
            else:
                parity.append(-parity[1])
            Fix+=[fix]
            Parity+=[parity]

        else:
            fix+=[s]
            if i%2==0:
                parity+=[1]
            else:
                parity+=[-1]
            Parity+=[parity]
            Fix+=[fix]
        fix=[0]
        parity=[1]
        s+=S[i]
    return (Fix,Parity)

