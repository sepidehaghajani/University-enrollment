import csv
from csv import DictWriter
import ast
import os


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as myfile:
            reader = csv.DictReader(myfile)
            return list(reader)


    def add_to_file(self, new_value):
        if isinstance(new_value, dict):
            fields = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            fields = new_value[0].keys()
        with open(self.file_path, 'a', newline="") as myfile:
            writer = DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(new_value)

    # def edit_row(self, updated_dict):
    #     all_rows = self.read_file()
    #     final_rows = []
    #     for row in all_rows:
    #         # information = ast.literal_eval(row["information"])
    #         # if information["address"]["postal_code"] == updated_dict["information"]["address"]["postal_code"]:
    #         row = updated_dict
    #         final_rows.append(row)
    #     self.add_to_file(final_rows, mode="w")