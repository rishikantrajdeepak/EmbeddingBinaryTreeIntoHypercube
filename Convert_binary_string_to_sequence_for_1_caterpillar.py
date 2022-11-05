def convert_binary_string_to_sequence_for_1_caterpillar(L):
    seq=[]
    n=len(L)
    i=-1
    j=0
    while j<n-1:
        if L[j]==1:
            seq.append(j-i)
            i=j
        j+=1
    seq.append(j-i)
    return seq
