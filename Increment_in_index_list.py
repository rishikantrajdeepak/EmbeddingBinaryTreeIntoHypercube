def increment_in_index_list(index_list,seq,size,last_index):
    index_list[last_index]+=1
    if index_list[last_index]<size[seq[last_index]-1]:
        return index_list
    elif last_index>0:
        index_list[last_index]=0
        last_index-=1
        increment_in_index_list(index_list,seq,size,last_index)
    return index_list
