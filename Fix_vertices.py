#input S the sequence for 1 caterpillar (first leg)
#Output 2 or 3 or 4 fixed vertices, along with parity, which will be mapped to fixed vertices in hypercube
#In particular outputs are [x,y] or [x,y,z] or [x,\alpha,y,z] along with parity

def fix_vertices(S):
    Fix=[] #list of lists of fixed vertices
    Parity=[] #list of lists of parity for each list of fixed vertices
    fix=[0] #first vertex, i.e. 0, is always fixed
    parity=[1] #first vertex 0 is given +1

    second=1 #second backbone vertex is always 1

    for i in range(1,len(S)): #i corresponds to i-th backbone vertex, begins with 1
        if S[i]==1:
            fix+=[second] #i-th backbone vertex is fixed
            if i%2==0: #i-th backbone is at even distance from 0
                parity+=[1]
            else: #i-th backbone is at odd distance from 0
                parity+=[-1]
            Fix+=[fix] #a list of fixed vertices added
            Parity+=[parity] #corresponding list of parity is added
        else:
            if i%2==1:
                fix+=[second,second+S[i]-1]
                if S[i]%2==0:
                    parity+=[-1,1]
                else:
                    parity+=[-1,-1]
            else:
                fix+=[second-S[i-1],second,second+S[i]-1]
                if S[i]%2==0:
                    parity+=[-1,1,-1]
                else:
                    parity+=[-1,1,1]
            Fix+=[fix]
            Parity+=[parity]
        fix=[0]
        parity=[1]
        second+=S[i]
    return (Fix,Parity)




