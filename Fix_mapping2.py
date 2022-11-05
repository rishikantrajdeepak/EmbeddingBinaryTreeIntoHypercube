#three vertices on the first leg are fixed and mapped to Qn

def fix_mapping(fixed_vertices,parity):
    if len(parity)==3:
        if -1 not in parity:
            fixed_map={fixed_vertices[0]:1,fixed_vertices[1]:2,fixed_vertices[2]:4}
        elif parity[0]==parity[1] and parity[1]!=parity[2]:
            fixed_map={fixed_vertices[0]:1,fixed_vertices[1]:2,fixed_vertices[2]:0}
        elif parity[0] !=parity[1] and parity[0]==parity[2]:
            fixed_map={fixed_vertices[0]:1,fixed_vertices[1]:0,fixed_vertices[2]:2}
        elif parity[0] !=parity[1] and parity[1]==parity[2]:
            fixed_map={fixed_vertices[0]:0,fixed_vertices[1]:1,fixed_vertices[2]:2}

    elif len(parity)==2:
        if -1 not in parity:
            fixed_map={fixed_vertices[0]:1,fixed_vertices[1]:2}
        elif -1 in parity:
            fixed_map={fixed_vertices[0]:0,fixed_vertices[1]:1}
    return fixed_map
