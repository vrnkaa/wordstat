

#dict_of_words = {i:list_of_words.count(i) for i in list_of_words}
#print(dict_of_words)

def convert_list_to_dict(list_of_words):
    temp=set(list_of_words)
    temp_list = list(temp)
    result={}
    for i in temp:
        result[i]=list_of_words.count(i)
        result[i]=temp_list.index(i)
    return result