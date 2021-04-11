import csv

def convert_dict_to_csv(dict_of_words):
    with open('dict.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in dict_of_words.items():
            writer.writerow([key, value])
    