import re

def convert_str_to_list(string_from_pdf):
    return re.findall(r'\w+', string_from_pdf)