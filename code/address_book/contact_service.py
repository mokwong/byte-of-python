import pickle

import contact


class ContactService:
    """联系人服务类。"""

    """封装了添加、删除、修改、分页列表、搜索、获取总数、序列化、反序列化联系人等方法"""

    def __init__(self, data_file_path='contact_list.data'):
        self.__contact_list_data_file = data_file_path
        self.__contact_list = self.__load_contact_list()

    def add_contact(self, name, gender, email, phone, birthday, address):
        contact_obj = contact.Contact(name, gender, email, phone, birthday, address)
        self.__contact_list.append(contact_obj)

    def remove_contact(self, index):
        assert 0 <= index < len(self.__contact_list)
        self.__contact_list.pop(index)

    def update_contact(self, index, name, gender, email, phone, birthday, address):
        assert 0 <= index < len(self.__contact_list)
        contact_obj = contact.Contact(name, gender, email, phone, birthday, address)
        self.__contact_list[index] = contact_obj

    def page_list(self, page_index, page_size=3):
        return self.__contact_list[(page_index - 1) * page_size: page_index * page_size]

    def search(self, keyword):
        return [c for c in self.__contact_list if keyword in str(c)]

    def count(self):
        return len(self.__contact_list)

    def save_contact_list(self):
        with open(self.__contact_list_data_file, 'wb') as f:
            pickle.dump(self.__contact_list, f)

    def __load_contact_list(self):
        try:
            with open(self.__contact_list_data_file, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No contact list data file found")
            return []
