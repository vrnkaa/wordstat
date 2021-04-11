import gspread


def write_to_googlesheets(dict_of_words):
    gc = gspread.service_account(filename="creds.json")
    sh = gc.open('testSheet').sheet1

    for key, value in dict_of_words.items():
            sh.append_row([key, value])

#sh.update('A1:A23','fjkgf')
