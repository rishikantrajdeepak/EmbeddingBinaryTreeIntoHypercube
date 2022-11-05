#main program, takes dimension of hypercube as input

import networkx as nx
import os
import time
from multiprocessing import Process
from Generate_hypercube_edgelist import generate_hypercube_edgelist
from Generate_sequences_for_1_caterpillars import generate_sequences_for_1_caterpillars
from Increment_in_index_list import increment_in_index_list
from Construct_1_caterpillar_from_sequence import construct_1_caterpillar_from_sequence as construct
#from Generate_powerset import generate_powerset
from Fix_vertices import fix_vertices  #fix all possible collection of two or three vertices in the first leg
#from Count_injective_homomorphisms import count_injective_homomorphisms as count_subgraph
from Is_subgraph import is_subgraph
from Fix_mapping import fix_mapping
import matplotlib.pyplot as plt

print('Enter the dimenension of the hypergraph:')
dimension_of_hypercube=int(input())
n=2**dimension_of_hypercube
#print(n)

#directory is created to store files
parent_directory=os.getcwd()
directory='caterpillars'
path=os.path.join(parent_directory,directory)
try:
    os.mkdir(path)
except OSError:
    print()

print('Directory created to store all text files in caterpillars folder\n')

#create hypercube of dimension n
hypercube_edgelist=generate_hypercube_edgelist(dimension_of_hypercube)
hypercube=nx.Graph()
hypercube.add_edges_from(hypercube_edgelist)

generate_sequences_for_1_caterpillars(n) #generate corresponding text files in folder caterpillars
print('Sequences corresponding to all possible legs of caterpillars created\n')

path=os.getcwd()+'/caterpillars/' #path to all files including 1 caterpillars

filehandles=[open(path+'cat'+str(k)+'.txt').readlines() for k in range(1,n+1)]
size=[len(file) for file in filehandles]
#size=[os.stat(path+'cat'+str(k)+'.txt').st_size for k in range(1,n+1)]
input_file=filehandles[-1]



n_process = 6
def parallel_function(sequence,file_number):
    
    seq=[int(x) for x in sequence.split()]
    index_list=[0]*len(seq)  #index for current line in each file
    while index_list[0]<size[seq[0]-1]:
        caterpillar_leg=[] #sequence for the current 1 caterpillar generated
        caterpillar_edgelist=[] #edgelist for the current perfectly balanced 2 caterpillar
        start_label=0 #start label for vertices in 1 caterpillar edgelist
        for k in range(len(seq)):
            if k==0:
                first_leg=[int(x) for x in filehandles[seq[k]-1][index_list[k]].split()]
                caterpillar_edgelist+=construct(first_leg,start_label)
            else:
                caterpillar_leg=[int(x) for x in filehandles[seq[k]-1][index_list[k]].split()]
                caterpillar_edgelist+=construct(caterpillar_leg,start_label)
            if k<len(seq)-1:
                caterpillar_edgelist+=[(start_label,start_label+seq[k])]
            start_label+=seq[k]
        (Fixed_vertices,Parity)=fix_vertices(first_leg) #stores list of lists of fixed vertices
        caterpillar=nx.Graph()
        caterpillar.add_edges_from(caterpillar_edgelist)

        for (fixed_vertices,parity) in zip(Fixed_vertices,Parity):
            fixed_map=fix_mapping(fixed_vertices,parity)
            truth_value=is_subgraph(caterpillar,hypercube,fixed_map)
            if truth_value==False or (time.localtime().tm_hour%5==0 and time.localtime().tm_min%59==0 and time.localtime().tm_sec%59==0):
                print(sequence,' : ',truth_value,' : ',index_list)


        index_list=increment_in_index_list(index_list,seq,size,len(seq)-1)  #increase index_list by one



for sequence_batch_start in range(0,size[-1], n_process):
    processes=[]
    for file_number,sequence in enumerate(input_file[sequence_batch_start : sequence_batch_start+n_process]):
        p = Process(target=parallel_function, args=(sequence,file_number))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

