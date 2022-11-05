#generate text file containing edges for hypercube
#Input is dimension n. Qn is halved into two Qn-1 and edges are added. This is recursive met    hod, and at each step 0x is attached to 1x, where x belongs to Qn-1 


def generate_hypercube_edgelist(n):
    edgelist=add_edges(0,n)
    return edgelist
 
edges=[]
def add_edges(a,n):
    global edges 
    edges+=[(x,x+pow(2,n-1)) for x in range(a,a+pow(2,n-1))]
    if n==1:
        return edges
    else:
        add_edges(a,n-1)
        add_edges(a+pow(2,n-1),n-1)
    return edges 




"""
import networkx as nx

def generate_hypercube_edgelist(n):
    G=nx.hypercube_graph(n)

    G_dict={}
    for node in G.nodes():
        G_dict[node]=len(G_dict)

    Edge_list=[]
    for edge in G.edges():
        Edge_list+=[(G_dict[edge[0]],G_dict[edge[1]])]
    return Edge_list
"""
