"""
    File Repository module
"""
from domain.entity import Person, Activity
from repository.inmemoryrepo import Repository


class FileRepository(Repository):
    def __init__(self, data_file):
        Repository.__init__(self)
        self.data_file = data_file

    def write_all_to_file(self):
        file = open(self.data_file, 'w')

        try:
            for entity in self.find_all():
                if isinstance(entity, Person):
                    person_str = entity.name + ';' + entity.phone_number + '\n'
                    file.write(person_str)
                elif isinstance(entity, Activity):
                    activity_str = str(entity.person_id_list) + ';' + entity.date + ';' + \
                                   entity.time + ';' + entity.description + '\n'
                    file.write(activity_str)

            file.close()
        except IOError as ex:
            print(ex)
            raise ex
