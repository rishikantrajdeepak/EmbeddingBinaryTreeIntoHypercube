def hamming_weight(L):
    count=0
    for l in L:
        if l==1:
            count+=1
    if L[-1]==0:
        count+=1
    return count
