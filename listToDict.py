import pdfconvert

#dict_of_words = {i:list_of_words.count(i) for i in list_of_words}
#print(dict_of_words)

def convert_list_to_dict():
    temp=set(pdfconvert.list_of_words)
    result={}
    for i in temp:
        result[i]=pdfconvert.list_of_words.count(i)
    print(result)