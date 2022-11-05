def construct_1_caterpillar_from_sequence(L,n):
    Edge_list=[]
    for l in range(len(L)):
        Edge_list+=[(n+i,n+i+1) for i in range(L[l]-1)]
        if l!=len(L)-1:
            Edge_list+=[(n,n+L[l])]
            n+=L[l]

    return Edge_list
