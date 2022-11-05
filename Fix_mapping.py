#input 2 or 3 or 4 fixed vertices in first leg
#output corresponding fixed vertices in hypercube, to be considered in any map later

def fix_mapping(fixed_vertices,parity):
    if len(fixed_vertices)==2:
        if parity[1]==-1:
            fixed_map={fixed_vertices[0]:0,fixed_vertices[1]:1}
        else:
            fixed_map={fixed_vertices[0]:0,fixed_vertices[1]:3}
    elif len(fixed_vertices)==3:
        if parity==[1,-1,1]:
            fixed_map={fixed_vertices[0]:1,fixed_vertices[1]:0,fixed_vertices[2]:2}
        else:  #else parity==[1,-1,-1]
            fixed_map={fixed_vertices[0]:0,fixed_vertices[1]:1,fixed_vertices[2]:2}
    elif len(fixed_vertices)==4:
        if parity==[1,-1,1,1]:
            fixed_map={fixed_vertices[0]:1,fixed_vertices[1]:0,fixed_vertices[2]:2,fixed_vertices[3]:4}
        else: #else parity==[1,-1,1,-1]
            fixed_map={fixed_vertices[0]:0,fixed_vertices[1]:1,fixed_vertices[2]:3,fixed_vertices[3]:2}
    
    return fixed_map
