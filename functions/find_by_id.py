def find_by_id(list_contacts, contact_id):
    for contact in list_contacts:
        if contact['id'] == contact_id:
            return contact
    return None
