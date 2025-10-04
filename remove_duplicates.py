# Remove Duplicates from list
def remove(in_list):
    out_list = []
    for item in in_list:
        if item not in out_list:
            out_list.append(item)
    return out_list

in_list = [1,2,3,4,5,1,2,3,4,5]
out_list = remove(in_list)
print(f"List after removing duplicates from {in_list} is {out_list}")
