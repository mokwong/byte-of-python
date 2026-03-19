class Contact:
    """联系人类。"""

    """包括姓名、性别、邮件地址、电话号码、生日、住址信息"""

    def __init__(self, name, gender, email, phone, birthday, address):
        self.name = name
        self.gender = gender
        self.email = email
        self.phone = phone
        self.birthday = birthday
        self.address = address

    def __str__(self):
        return f"Contact@{self.name} {self.gender} {self.email} {self.phone} {self.birthday} {self.address}"
