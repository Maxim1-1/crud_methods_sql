class Utils:
    @staticmethod
    def get_test_with_equal_id(data, count_elements):
        """returns test ids that contain the same digits, for example 11, 77
        count_elements - how many identical tests do you want to get """
        new = []
        for i in data:
            value = list(str(i[0]))
            if len(set(value)) == 1 and i[0] > 10:
                new.append(i)
            if len(new) == count_elements:
                break
        return new

    @staticmethod
    def replace_author_and_project_test(tests, author, project):
        new_list = []
        for i in tests:
            new_obj = list(i)
            new_obj[-7], new_obj[-1] = project, author
            new_list.append(tuple(new_obj))
        return new_list

    @staticmethod
    def convert_result_test_in_number(test):
        """translating a text result into a number
        if the test has passed, it will be assigned the status_id = 1,
        if the test has fallen, it will be assigned the status_id = 2
        if the test has skipped, it will be assigned the status_id = 3"""

        if test == 1:
            return 2
        elif test == 0:
            return 1
        else:
            return 3
