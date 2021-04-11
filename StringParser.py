import csv
import re


class StringParser:

    @classmethod
    def to_list(cls, string_from_pdf: str) -> list:
        return re.findall(r'\w+', string_from_pdf)

    @classmethod
    def to_unique_list(cls, string_from_pdf: str) -> list:
        return list(set(StringParser.to_list(string_from_pdf)))

    @classmethod
    def to_dict(cls, string_from_pdf: str) -> dict:
        temp = set(StringParser.to_list(string_from_pdf))
        result = {}
        for i in temp:
            result[i] = StringParser.to_list(string_from_pdf).count(i)
        return result

    @classmethod
    def dict_to_csv(cls, string_from_pdf: str):
        with open('dict.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in StringParser.to_dict(string_from_pdf).items():
                writer.writerow([key, value])


