#INPUT: pattern graph Domain_graph, Host_graph, dictionary fixed_map for fixing maps of at most 4 vertices

import networkx as nx
import numpy as np

def is_subgraph(Guest_graph,Host_graph,fixed_pattern):
    
    Guest_matrix=np.asarray(nx.to_numpy_matrix(Guest_graph))
    Host_matrix=np.asarray(nx.to_numpy_matrix(Host_graph))

    step=1
    while True:
        if step == 1:
            dimension=len(Guest_matrix) #p dimension of square transition matrix
            Transition_matrix=np.ones([dimension,dimension]) #M the transition matrix being created
            Transition_matrix_at_depth={} #M_d stores transition matrix after a change in the d-th row at depth d
            depth=0 #p depth of the tree with root at depth 0, depth = row of transition matrix being changed
            Column_selected_at_depth=[-1] #H column of tansition matrix being selected at depth d, may be or may not be used
            Column_used=[0]*dimension #F column of transition matrix used 
            step=2
        
        if step == 2:
            for column in range(dimension):
                if Transition_matrix[depth,column]==1 and Column_used[column]==0:
                    Transition_matrix_at_depth[depth]=np.copy(Transition_matrix)
                    if depth == 0:
                        current_column=Column_selected_at_depth[0] #a column is selected at depth=0
                    else:
                        current_column=-1 #no column selected at depth
                    step=3
                    break
            else:
                step=7
        
        if step == 3:
            current_column+=1
            while Transition_matrix[depth,current_column]==0 or Column_used[current_column]==1:
                current_column+=1
            for column in range(dimension):
                if column != current_column:
                    Transition_matrix[depth,column]=0
            step=4

        if step == 4:
            if depth<dimension-1:
                step=6
            else:
                print('Reached isomorphism check')
                input()
                Mapping_matrix=np.dot(Transition_matrix,np.transpose(np.dot(Transition_matrix,Host_matrix))) #C=M(B^tM^t)
                truth_value=True
                for row in range(dimension):
                    for column in range(dimension):
                        if Domain_matrix[i][j]==1:
                            if Host_matrix[i][j]==1:
                                pass
                            else:
                                print('reached false assignment')
                                input()
                                truth_value=False
                                break
                    if truth_value==False:
                        step=5
                        break
                print('Reached to check True')
                if truth_value==True:
                    return True
        
        if step == 5:
            for column in range(current_column+1,dimension):
                if Transition_matrix[depth,column]==1 and Column_used[column]==0:
                    Transition_matrix=np.copy(Transition_matrix_at_depth[depth])
                    step=3
                    break
            else:
                step=7

        if step == 6:
            Column_selected_at_depth[depth]=current_column
            Column_used[current_column]=1
            depth+=1
            step=2

        if step == 7:
            if depth==0:
                return False
            else:
                Column_used[current_column]=0
                depth-=1
                Transition_matrix=np.copy(Transition_matrix_at_depth[depth])
                current_column=Column_selected_at_depth[depth]
                current_column=Column_selected_at_depth[depth]
                step=5

