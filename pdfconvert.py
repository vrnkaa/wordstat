
import listToDict
import pdfToStr
import strToList

str_from_pdf = pdfToStr.convert_pdf_to_str()
list_of_words = strToList.convert_str_to_list(str_from_pdf)
dict_of_words = listToDict.convert_list_to_dict(list_of_words)

print(dict_of_words)

