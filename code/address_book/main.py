import contact_book

contact_book_obj = contact_book.ContactBook()

while True:
    contact_book_obj.display_menu()
    op_code = int(input())
    if op_code == 6:
        contact_book_obj.exit()
        break
    elif op_code == 2:
        contact_book_obj.add()
    elif op_code == 3:
        contact_book_obj.update()
    elif op_code == 4:
        contact_book_obj.delete()
    elif op_code == 5:
        contact_book_obj.search()
    elif op_code == 1:
        contact_book_obj.page_list()
    else:
        print("无效的选项，请重新输入")
