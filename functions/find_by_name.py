def find_by_name(list_contacts, contact_name):
    found_contacts_list = []
    for contact in list_contacts:
        if contact['name'].lower() == contact_name.lower():
            found_contacts_list.append(contact)
    return found_contacts_list