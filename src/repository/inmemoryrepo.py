"""
    In-memory Repository module
"""
from domain.data_structure import MyDataStructure, DataStructureService


class Repository:
    def __init__(self):
        self.__entities = MyDataStructure()
        self.__entities_service = DataStructureService(self.__entities)

    def find_by_id(self, entity_id):
        # return self.__entities[int(entity_id)]
        for element in self.find_all():
            if element.id == entity_id:
                return element

    def save(self, entity):
        # self.__entities[int(entity.id)] = entity
        self.__entities.__add__(entity)

    def delete_by_id(self, entity_id):
        self.__entities.__delitem__(int(entity_id))

    def update(self, entity_id, entity):
        self.__entities.update(entity_id, entity)

    def find_all(self):
        return self.__entities.get_all_elements()

    def sort(self):
        self.__entities_service.shell_sort(self.__entities_service.compare_by_ids)

    def filter_greater_id(self, args):
        self.__entities_service.filter(self.__entities_service.id_greater_than, args)
