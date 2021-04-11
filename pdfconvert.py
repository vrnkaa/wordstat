
import listToDict
import pdfToStr
import strToList
import dictToCsv
import dictToGoogleTables
import uniqueValueList


str_from_pdf = pdfToStr.convert_pdf_to_str()
list_of_words = strToList.convert_str_to_list(str_from_pdf)
#dict_of_words = listToDict.convert_list_to_dict(list_of_words)
#dictToCsv.convert_dict_to_csv(dict_of_words)
list_of_unique_words = uniqueValueList.to_unique_value_list(list_of_words)

print(list_of_words)
print(len(list_of_words))


print(list_of_unique_words)
print(len(list_of_unique_words))
