import os

from storages.storage import Storage
import json

class FileStorage(Storage):

    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        if not os.path.exists(self.file_name):
            raise StopIteration

        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                yield line.strip()


    def write_json(self, data_arr):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for data in data_arr:
                f.write(json.dumps(data, ensure_ascii=False)+'\n')


    def write_data(self, data_array):
        """
        :param data_array: collection of strings that
        should be written as lines
        """
        with open(self.file_name, 'w') as f:
            for line in data_array:
                if line.endswith('\n'):
                    f.write(line)
                else:
                    f.write(line + '\n')

    def append_data(self, data):
        """
        :param data: string
        """
        with open(self.file_name, 'a') as f:
            for line in data:
                if line.endswith('\n'):
                    f.write(line)
                else:
                    f.write(line + '\n')
