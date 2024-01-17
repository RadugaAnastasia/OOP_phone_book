import text
import view
import model

def find_contact():
    word = view.input_data(text.input_search_word)
    result = model.find_contact(word)
    view.show_contacts(result, text.contacts_not_found(word))

def start_app():
    while True:
        choice = view.main_menu()
        if choice == 1:
            model.open_file()
            view.print_message(text.load_successful)
        if choice == 2:
            model.save_file()
            view.print_message(text.save_successful)
        if choice == 3:
            pb = model.phone_book
            view.show_contacts(pb, text.empty_phone_book)
        if choice == 4:
            contact = view.add_contact(text.new_contact)
            model.new_contact(contact)
            view.print_message(text.new_contact_added_successful(contact[0]))
        if choice == 5:
            find_contact()
        if choice == 6:
            find_contact()
            pb = model.phone_book
            c_id = int(view.input_data(text.input_id_change_contact))
            c_contact = view.add_contact(text.change_contact_contact, pb[c_id])
            model.change_contact(c_id, c_contact)
            view.print_message(text.contact_changed_successful(c_contact[0]))
        if choice == 7:
            find_contact()
            c_id = int(view.input_data(text.input_id_delete_contact))
            name = model.delete_contactct(c_id)[0]
            view.print_message(text.contact_deleted_successful(name))
        if choice == 8:
            view.print_message(text.good_bye)
            break





