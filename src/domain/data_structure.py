"""
    Data structure module
"""


class MyDataStructure:
    class MyIterator:
        def __init__(self, data_struct):
            self._data_structure = data_struct
            self._poz = 0

        def __next__(self):
            # Stop iteration when elements are no longer available
            if self._poz == len(self._data_structure):
                raise StopIteration

            # Else, move to next element
            self._poz += 1
            return self._data_structure[self._poz - 1]

    def __init__(self):
        self._data = []

    def __add__(self, element):
        self._data.append(element)

    def __iter__(self):
        return self.MyIterator(self)

    def __setitem__(self, element_index, value):
        self._data[element_index] = value

    def __getitem__(self, elem_index):
        return self._data[elem_index]

    def __delitem__(self, elem_id):
        for element in self._data:
            if element.id == elem_id:
                self._data.remove(element)
                return

    def __len__(self):
        return len(self._data)

    def get_all_elements(self):
        return self._data

    def update(self, element_id, value):
        for index in range(len(self._data)):
            if self._data[index].id == element_id:
                self._data[index] = value


class DataStructureService:
    def __init__(self, data_structure):
        self._data_structure = data_structure

    @staticmethod
    def compare_by_ids(elem1, elem2):
        """
        Returns True if the id of element 1 is less than or equal to
        the id of element 2, and False otherwise.
        """
        return elem1.id <= elem2.id

    @staticmethod
    def id_greater_than(element, reference_id):
        """
        Returns True if the element's id is greater than the reference id,
        and False otherwise
        """
        return element.id > int(reference_id)

    def shell_sort(self, comparison_function):
        list_length = len(self._data_structure)

        # Initializing list of gaps (Ciura's gaps)
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]

        # Start with the largest gap, and go down to 1
        for gap in gaps:
            # For each gap, perform an insertion sort on the subsequences of the array containing
            # elements whose indexes go from "gap" to "gap". For example, if gap is 4,
            # a possible subsequence is (a1, a5, a9, ....). The subsequence will be parsed in reverse order,
            # and if we find 2 elements that are in the wrong order, we shift the larger element to the right,
            # and at the end we place the right-far most element on the correct position of the subsequence (if needed).
            for i in range(gap, list_length):
                # save self._data_structure[i] (it will be overwritten, if we perform right shifting of elements),
                # so we can place it  at the correct position in the end
                temp = self._data_structure[i]

                # shift elements in the subsequence up, until we find the right position for "temp"
                j = i
                while j >= gap and comparison_function(self._data_structure[j - gap], temp) is False:
                    self._data_structure[j] = self._data_structure[j - gap]
                    j -= gap

                # place "temp" in the correct position in the sorted list
                self._data_structure[j] = temp

    def filter(self, filter_function, args):
        x = 0
        while x < len(self._data_structure):
            if filter_function(self._data_structure[x], *args) is False:
                self._data_structure.__delitem__(self._data_structure[x].id)
            else:
                x += 1
