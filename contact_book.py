import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Class for handling contact information.
class Contact_info():

    def __init__(self):
        # CSV File for storing contact data.
        self.file_path = 'contact_info.csv'

        # Column names for the CSV File.
        self.columns = ['Name','Phone','Email','Address']

        # Try reading the existing CSV File.
        try:
            self.contacts_data = pd.read_csv(self.file_path)
        except FileNotFoundError:

            # If it does not exist, create a new CSV file with column names.
            self.contacts_data = pd.DataFrame(columns=self.columns)

            # Save the empty dataframe.
            self.save_contacts_data()
    
    # Save the contact data to the CSV file.
    def save_contacts_data(self):

        self.contacts_data.to_csv(self.file_path,index=False)

    # Add a new contact to the data and save it to the CSV File.
    def add_contact(self,name,phone,email,address):
        new_contact = pd.DataFrame([[name, phone, email, address]], columns=self.columns)

        # Concatenate the new contact with the exsisting data.
        self.contacts_data = pd.concat([self.contacts_data, new_contact], ignore_index=True)

        # Save the updated contact list.
        self.save_contacts_data()
    
    # Search for the contact by name or phone.
    def find_contact(self,search):

        # Filter contact data for matches in either 'Name' or 'Phone' columns.
        results = self.contacts_data[(self.contacts_data["Name"].astype(str).str.contains(search,case=False,na=False)) |
                                     (self.contacts_data["Phone"].astype(str).str.contains(search,case=False,na=False))]
        return results

    # Update a contact's information by their name.
    def update_contact(self,name,phone,email,address):
        index = self.contacts_data[self.contacts_data['Name'] == name].index
        if not index.empty:

            # Update the contact at the found index.
            self.contacts_data.at[index[0],'Phone'] = phone
            self.contacts_data.at[index[0],'Email'] = email
            self.contacts_data.at[index[0],'Address'] = address

            # Save the updated contact data.
            self.save_contacts_data()

    # Remove a contact from the data by name
    def remove_contact(self,name):

        # Filter out the contact with the given name.
        self.contacts_data = self.contacts_data[self.contacts_data['Name'] != name]

        # Save the updated contact data.
        self.save_contacts_data()

# GUI Class for managing the Contact Book.
class ContactGUI:
    
    def __init__(self,root):
        
        # Initial setup of the GUI window.
        self.root = root
        self.root.title("Contact Book")

        # Create an instance of the Contance_info class to manage the data.
        self.contacts = Contact_info()

        # Initialize the widgets (UI components).
        self.create_widgets()

    def create_widgets(self):

         # Create all the necessary widgets for the GUI (labels, entries, buttons).
        self.search_label = tk.Label(self.root,text = "Search(Name/Phone): ",font=("Arial",12))
        self.search_label.grid(row=0, column=0, padx=5, pady=5)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='ew')
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.search_button = tk.Button(self.root,text="Search",command=self.find_contact,font=("Arial",12))
        self.search_button.grid(row=1,column=1,padx=5, pady=5,sticky='ew')

        self.add_label = tk.Label(self.root,text="Add New Contact",font=("Arial",18,"bold"))
        self.add_label.grid(row=2,column=0,columnspan=4, padx=5, pady=5)

        # Labels and entry fields for adding new contacts.
        self.name_label = tk.Label(self.root,text="Name",font=("Arial",12))
        self.name_label.grid(row=3,column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=3,column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.root,text="Phone",font=("Arial",12))
        self.phone_label.grid(row=4,column=0)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=4,column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.root,text="Email",font=("Arial",12))
        self.email_label.grid(row=5,column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=5,column=1, padx=5, pady=5)

        self.address_label = tk.Label(self.root,text="Address",font=("Arial",12))
        self.address_label.grid(row=6,column=0)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=6,column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.root,text="Add Contact",command=self.add_contact,font=("Arial",12))
        self.add_button.grid(row=7,column=0,columnspan=3, padx=5, pady=5)

        # Listbox to display contacts.
        self.contact_listbox = tk.Listbox(self.root,height=10,width=40)
        self.contact_listbox.grid(row=8,column=0,columnspan=3, padx=5, pady=5,sticky="nsew")

        # Scrollbar for the listbox.
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.contact_listbox.yview)
        self.scrollbar.grid(row=8, column=3, sticky="ns")

        # Buttons for additional functionalities.
        self.prefill_button = tk.Button(self.root, text="Pre-fill Fields", command=self.pre_fill_fields,font=("Arial",12))
        self.prefill_button.grid(row=9, column=0, padx=5, pady=5, sticky='ew')

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact,font=("Arial",12))
        self.update_button.grid(row=9, column=1, padx=5, pady=5, sticky='ew')

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact,font=("Arial",12))
        self.delete_button.grid(row=9, column=2, padx=5, pady=5, sticky='ew')

        # Set column weights for expanding the interface.
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def add_contact(self):

        # Collect and validate the data for adding a new contact.
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        # Validate required fields.
        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required fields!")
            return

        # Validate phone number format.
        if not phone.isdigit() or len(phone) < 7 or len(phone) > 15:
            messagebox.showerror("Error", "Phone number must be numeric and between 7 to 15 digits.")
            return

        # Validate email format.
        if email:
            import re
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, email):
                messagebox.showerror("Error", "Invalid email format!")
                return

        # Add the contact and clear input fields.
        self.contacts.add_contact(name, phone, email, address)
        self.clear_entries()
        self.find_contact()
        messagebox.showinfo("Success", "Contact added successfully!")

    def find_contact(self):

        # Find contacts based on search query.
        query = self.search_entry.get()
        results = self.contacts.find_contact(query)
        self.contact_listbox.delete(0, tk.END)

        # Show all contacts if no search query is provided.
        if not query.strip():
            results = self.contacts.contacts_data  # Show all contacts
        else:
            results = self.contacts.find_contact(query)
        
        # Display the search results.
        if results.empty:
            self.contact_listbox.insert(tk.END, "No matching contacts found.")
        else:
            for _, row in results.iterrows():
                self.contact_listbox.insert(tk.END, f"{row['Name']} - {row['Phone']} - {row['Email']} - {row['Address']}")


    def delete_contact(self):

        # Delete a selected contact from the listbox.
        selected = self.contact_listbox.curselection()
        if selected:
            try:
                name = self.contact_listbox.get(selected[0]).split(" - ")[0]
                self.contacts.remove_contact(name)
                self.find_contact()
            except IndexError:
                messagebox.showerror("Error", "Invalid selection.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def update_contact(self):

        # Update a selected contact from the listbox.
        selected = self.contact_listbox.curselection()
        if selected:
            name = self.contact_listbox.get(selected[0]).split(" - ")[0]
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if phone:
                self.contacts.update_contact(name,phone,email,address)
                self.find_contact()
            else:
                messagebox.showerror("Error", "Phone number is required.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def clear_entries(self):

        # Clear the input fields after adding/updating a contact.
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def pre_fill_fields(self):

        # Pre-fill the input fields with the selected contact's data.
        selected = self.contact_listbox.curselection()
        if selected:
            try:
                contact = self.contact_listbox.get(selected[0])
                name, phone, email, address = contact.split(" - ")
                
                # Pre-fill the entry fields.
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                
                self.phone_entry.delete(0, tk.END)
                self.phone_entry.insert(0, phone)
                
                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, email)
                
                self.address_entry.delete(0, tk.END)
                self.address_entry.insert(0, address)
            except ValueError:
                messagebox.showerror("Error", "Invalid contact format in Listbox.")
        else:
            messagebox.showerror("Error", "Please select a contact to pre-fill.")

if __name__ == "__main__":
    # Run the application.
    root = tk.Tk()
    gui = ContactGUI(root)
    root.mainloop()