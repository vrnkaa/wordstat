from gspreadsheet import GSpreadsheet


def write_dict_to_google_table(dict_of_words):
    reader = GSpreadsheet("https://docs.google.com/myspreadsheet")
    for row in reader:
        #process(row)
