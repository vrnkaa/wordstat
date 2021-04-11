from StringParser import StringParser
import pdfToStr


l: list = StringParser.to_list(pdfToStr.pdf_to_str('sample2.pdf'))
print(list)