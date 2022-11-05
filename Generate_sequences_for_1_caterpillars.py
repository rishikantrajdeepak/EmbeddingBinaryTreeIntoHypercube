#we can optimize the code by running for fixed n (not depending on k). For that we need to look for first_index having 1, including left will give result for n, and excluding left of first_index will give me result for (n-first_index)

import os
#from Hamming_weight import hamming_weight as H
from Convert_binary_string_to_sequence_for_1_caterpillar import convert_binary_string_to_sequence_for_1_caterpillar as cat
from Truth_value import truth_value as value


path=os.getcwd()+'/caterpillars/'

def generate_sequences_for_1_caterpillars(n):
    
    filehandles=[open(path+'cat'+str(k)+'.txt','w') for k in range(1,n+1)]
    
    L=[0]*(n-1)+[1] #binary strings of length n

    while L!=[1]*n:
        i=n-1 #checks consecutive entry 1 from right to left
        while L[i]==1:
            L[i]=0
            i-=1
        L[i]=1
        if L[-1]==1:
            seq=cat(L)
            balance=value(seq[0:])
            if balance=='True':
                if seq[0]>5:
                    filehandles[-1].writelines(['%s '%x for x in seq])
                    filehandles[-1].write('\n')

                if seq[1]==1:
                    filehandles[n-seq[0]-1].writelines(['%s '%x for x in seq[1:]])
                    filehandles[n-seq[0]-1].write('\n')
    
    for files in filehandles:
        files.close()

