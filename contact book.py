import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, index):
        del self.contacts[index]

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    if name and phone:
        contact = Contact(name, phone, email, address)
        contact_manager.add_contact(contact)
        messagebox.showinfo("Success", "Contact added successfully.")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Please enter name and phone number.")

def delete_contact():
    index = contact_listbox.curselection()
    if index:
        contact_manager.delete_contact(index[0])
        messagebox.showinfo("Success", "Contact deleted.")
        display_contacts()

def update_contact():
    index = contact_listbox.curselection()
    if index:
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        if name and phone:
            contact = Contact(name, phone, email, address)
            contact_manager.update_contact(index[0], contact)
            messagebox.showinfo("Success", "Contact updated successfully.")
            clear_entries()
            display_contacts()
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

def search_contact():
    keyword = entry_search.get()
    if keyword:
        results = contact_manager.search_contact(keyword)
        if results:
            display_contacts(results)
        else:
            messagebox.showinfo("No Results", "No contacts found matching the search criteria.")
    else:
        messagebox.showerror("Error", "Please enter a search keyword.")

def display_contacts(contacts=None):
    contact_listbox.delete(0, tk.END)
    contacts_to_display = contacts if contacts else contact_manager.contacts
    for contact in contacts_to_display:
        contact_listbox.insert(tk.END, f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n\n")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_search.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Contact Manager")

# Create entry widgets
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=3, column=1, padx=5, pady=5)

label_search = tk.Label(root, text="Search:")
label_search.grid(row=4, column=0, padx=5, pady=5)
entry_search = tk.Entry(root, width=30)
entry_search.grid(row=4, column=1, padx=5, pady=5)

# Create buttons
button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.grid(row=0, column=2, padx=5, pady=5)

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
button_delete.grid(row=1, column=2, padx=5, pady=5)

button_update = tk.Button(root, text="Update Contact", command=update_contact)
button_update.grid(row=2, column=2, padx=5, pady=5)

button_search = tk.Button(root, text="Search", command=search_contact)
button_search.grid(row=4, column=2, padx=5, pady=5)

# Create view contact list button
button_view = tk.Button(root, text="View Contact List", command=display_contacts)
button_view.grid(row=3, column=2, padx=5, pady=5)

# Create contact listbox
contact_listbox = tk.Listbox(root, width=60, height=15)
contact_listbox.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Initialize contact manager
contact_manager = ContactManager()

root.mainloop()
