from StringParser import StringParser
import pdfToStr


str_from_pdf = pdfToStr.pdf_to_str()

csv_file = StringParser.dict_to_csv(str_from_pdf)