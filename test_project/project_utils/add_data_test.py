class UtilsData:
    @staticmethod
    def add_author_project(selected_test, last_id, author, project):
        new_list = []
        for index, el in enumerate(selected_test):
            new = list(el)
            new[0] = (last_id + index) + 1
            new[-1] = author
            new[-7] = project
            new_list.append(tuple(new))

        return new_list
