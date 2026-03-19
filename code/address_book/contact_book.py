import math

import contact_service


def print_contact_list(contact_list):
    """打印，中文对齐是个难题呀！"""
    print("--------------------")
    format_string = "{: ^4}\t{: ^5}\t{: ^2}\t{: ^11}\t{: ^10}\t{: ^20}\t{: ^30}"
    print(format_string.format("用户id", "姓名", "性别", "电话号码", "生日", "住址信息", "邮件地址"))
    for i in range(0, len(contact_list)):
        print(format_string.format(i, contact_list[i].name, contact_list[i].gender,
                                   contact_list[i].phone, contact_list[i].birthday, contact_list[i].address,
                                   contact_list[i].email))
    print("--------------------")


class ContactBook:
    """地址簿类"""

    def __init__(self, data_file_path='contact_list.data'):
        self.__contact_service = contact_service.ContactService(data_file_path)

    def display_menu(self):
        first_line = "\n欢迎使用地址簿程序，当前地址簿总共有 {} 个联系人，请选择你需要的功能："
        print(first_line.format(self.__contact_service.count()))
        print("1. 联系人分页列表")
        print("2. 添加联系人")
        print("3. 编辑联系人")
        print("4. 删除联系人")
        print("5. 搜索联系人")
        print("6. 退出")

    def exit(self):
        self.__contact_service.save_contact_list()
        print("感谢使用，欢迎下次再来，再见")

    def add(self):
        print("请输入姓名（最多4个字符）：", end="")
        name = input()
        print("请输入性别（男/女）：", end="")
        gender = input()
        print("请输入邮件地址（最多30个字符）：", end="")
        email = input()
        print("请输入电话号码（11个字符）：", end="")
        phone = input()
        print("请输入生日（yyyy-MM-dd）：", end="")
        birthday = input()
        print("请输入住址信息（最多20个字符）：", end="")
        address = input()
        self.__contact_service.add_contact(name, gender, email, phone, birthday, address)
        print("添加成功！")

    def update(self):
        print("请输入需要修改的联系人id：", end="")
        index = int(input())
        print("请输入新的姓名（最多4个字符）：", end="")
        name = input()
        print("请输入新的性别（男/女）：：", end="")
        gender = input()
        print("请输入新的邮件地址（最多30个字符）：", end="")
        email = input()
        print("请输入新的电话号码（11个字符）：", end="")
        phone = input()
        print("请输入新的生日（yyyy-MM-dd）：", end="")
        birthday = input()
        print("请输入新的住址信息（最多20个字符）：", end="")
        address = input()
        self.__contact_service.update_contact(index, name, gender, email, phone, birthday, address)
        print("编辑成功！")

    def delete(self):
        print("请输入需要删除的联系人id：", end="")
        index = int(input())
        self.__contact_service.remove_contact(index)
        print("删除成功！")

    def search(self):
        print("请输入需要搜索的信息：", end="")
        keyword = input()
        contacts = self.__contact_service.search(keyword)
        print("搜索结果如下：")
        print_contact_list(contacts)

    def page_list(self, page_index=1, page_size=3):
        while True:
            page_records = self.__contact_service.page_list(page_index, page_size)
            print_contact_list(page_records)
            total_pages = math.ceil(self.__contact_service.count() / page_size)
            print("当前页号：{}，总页数：{}，输入 b 返回上一页，输入 n 进入下一页 输入 q 退出列表".format(page_index, total_pages))
            page_list_op_code = input()
            if page_list_op_code == 'q':
                print("退出列表成功！")
                break
            elif page_list_op_code == 'b':
                page_index = page_index - 1
                if page_index < 1:
                    print("已处于第一页，无法返回上一页")
                    page_index = 1
            elif page_list_op_code == 'n':
                page_index = page_index + 1
                if page_index > total_pages:
                    print("已处于最后一页，无法进入下一页")
                    page_index = total_pages
