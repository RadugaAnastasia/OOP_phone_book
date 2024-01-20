
class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_str(self, sep: str = ' '):
        return f'{self.name}{sep}{self.phone}{sep}{self.comment}'
    
    def field_len(self, field: str):
        if field == 'name':
            return len(self.name)
        elif field == 'phone':
            return len(self.phone)
        elif field == 'comment':
            return len(self.comment)

# OOP_Phone_book/model.py

class PhoneBook:
    def __init__(self, path: str = 'OOP_Phone_book/phones.txt', separator: str = ';'):
        self.phonebook = {}
        self.path = path
        self.separator = separator

    def open_file(self):
        with open(self.path, 'r', encoding = 'UTF-8') as file:
            for c_id, contact in enumerate(file.readlines(), 1):
                contact = contact.strip().split(self.separator)
                self.phonebook[c_id] = Contact(*contact)

    def save_file(self):
        data = []
        for contact in self.phonebook.values():
            data.append(contact.to_str(self.separator))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding = 'UTF-8') as file:
            file.write(data)


    def next_id(self):
        return (max(self.phonebook) + 1) if self.phonebook else 1

    def new_contact(self, contact: list[str]):
        self.phonebook[self.next_id()] = Contact(*contact)

    def find_contact(self, word: str) -> 'PhoneBook':
        result = PhoneBook()
        for u_id, contact in self.phonebook.items():
            if word.lower() in str(contact.to_str()).lower():
                result.phonebook[u_id] = Contact(*contact)
        return result

    def change_contact(self, c_id: int, c_contact: list[str]):
        self.phonebook[c_id] = Contact(*c_contact)

    def delete_contact(self, c_id: int) -> list[str]:
        return self.phonebook.pop(c_id)

    def max_len(self):
        max_field_lens = [0, 0, 0]
        for contact in self.phonebook.values():
            for n, field in enumerate(['name', 'phone', 'comment']):
                if max_field_lens[n] < contact.field_len(field):
                    max_field_lens[n] = contact.field_len(field)
        return max_field_lens