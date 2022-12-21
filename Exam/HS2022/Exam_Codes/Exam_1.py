def padded_dict(keys, values, padding=None):
    dic = {}
    key_list = keys.copy()
    values_list = values.copy()
    if len(values) < len(keys):
        for i in range(len(keys)-len(values)):
            values_list.append(padding)

    for key, value in zip(key_list, values_list):
        dic[key]=value
    
    return dic

   
    

