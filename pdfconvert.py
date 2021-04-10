import re
from listToDict import *

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open('sample2.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)


string_from_pdf = output_string.getvalue().lower()

list_of_words = re.findall(r'\w+', string_from_pdf)

#print(list_of_words)
print(len(list_of_words))
#print(len(set(list_of_words)))
#print(set(list_of_words))

#list_of_words.sort()
#print(list_of_words)




