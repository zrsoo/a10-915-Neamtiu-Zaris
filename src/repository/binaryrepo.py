"""
    Binary files repository module
"""
import pickle

from repository.inmemoryrepo import Repository


class BinaryFilesRepository(Repository):
    def __init__(self, data_file):
        Repository.__init__(self)
        self.data_file = data_file

    def write_all_to_file(self):
        file = open(self.data_file, "wb")
        pickle.dump(list(self.find_all()), file)
        file.close()

    def get_greatest_id(self):
        li_values = list(self.find_all())
        last_index = len(li_values) - 1
        if len(li_values) == 0:
            return 0
        return li_values[last_index].id
