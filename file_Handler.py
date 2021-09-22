import csv
from csv import DictWriter
class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as myfile:
            reader = csv.DictReader(myfile)
            print(list(reader))

    def add_to_file(self, new_value):
        if isinstance(new_value, dict):
            fields = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            fields = new_value[0].keys()

        with open(self.file_path, 'a') as myfile:

            writer = DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(new_value)

# def test_module():
#     print('this is from file_handler.py')

# test = FileHandler()
# test.add_to_file([{'name1': 'delaram', 'user1': "delaram"}, {'name1': 'kimia', 'user1': "kimia"}])
