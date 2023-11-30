#
# WELCOME TO THE GUARDIAN DIRECTORY
# This programme is designed to serve as a phonebook that keeps parental and guardian records of students enroled in Early Learning Centres.
#-----------
# The GUI and code for the Guardian Directory were inspired by the tutorials from https://www.youtube.com/@samcodehub and geekedu.org.(direct links can be found in the README.md file).
# A big thank you to https://github.com/michael305y, who helped fixed my code, made the Search and Sort functions work, as well as recommended adding the View and Clear functions.
#------------
# If you cannot run the code on Codio, kindly run it on PyCharm, where it was written.
#------------
#---code starts below this line---#


from tkinter import *

# GUI
root = Tk()
root.geometry('550x390')
root.title('Guardian Directory')
root.config(bg='light grey')
root.resizable(0, 0)

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=15, )
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


# list of existing contacts
GuardianDirectory = [
    ['De Leon', 'Drew', '4567891', 'address4', 'drew@deleon.com'],
    ['Appleby', 'Apple', '1234567', 'address1', 'apple@appleby.com'],
    ['Edogawa', 'Elle', '5678912', 'address5', 'elle@edogawa.com'],
    ['Cranston', 'Catherine', '3456789', 'address3', 'catherine@cranston.com'],
    ['Bartholomew', 'Brad', '2345678', 'address2', 'brad@bartholomew.com'],
    ]

LastName = StringVar()
FirstName = StringVar()
ContactNumber = StringVar()
Address = StringVar()
Email = StringVar()


# functions


# for displaying contacts in the list box
def display():
    #GuardianDirectory.sort()
    select.delete(0, END)
    for LastName, FirstName, ContactNumber, Address, Email in GuardianDirectory:
        select.insert(END,LastName + ', ' + FirstName)
display()


# selecting a contact
def selected():
    return int(select.curselection()[0])


# adding a contact
def add():
    GuardianDirectory.append([LastName.get(), FirstName.get(), ContactNumber.get(), Address.get(), Email.get()])
    display()
    print("Successfully added new contact.")
    clear_fields()


# deleting a contact
def delete():
    try:
        del GuardianDirectory[selected()]
        display()
        clear_fields()
        print("Contact deleted.")
    except IndexError:
        print("No contact was selected.")


# searching a contact
def search():
    search_result = LastName.get()
    for contact in GuardianDirectory:
        if search_result == contact[
            0]:
            print(f'Displaying {search_result} contact information.')

            LastName.set(contact[0])
            FirstName.set(contact[1])
            ContactNumber.set(contact[2])
            Address.set(contact[3])
            Email.set(contact[4])
            return
    clear_fields()
    print(f'{search_result} Not found.')

def sortsearch():
    GuardianDirectory.sorted()
    select.delete(0, END)
    for FirstName, LastName, ContactNumber, Address, Email in GuardianDirectory:
        select.insert(END,LastName)


# sorting contact last names in descending order
def sorting():
    GuardianDirectory.sort(reverse=True)
    select.delete(0, END)
    for FirstName, LastName, ContactNumber, Address, Email in GuardianDirectory:
        select.insert(END, FirstName)
    print("Contact last names are sorted in descending order.")


# viewing contact details
def view():
    try:
        LASTNAME, FIRSTNAME, CONTACTNNUMBER, ADDRESS, EMAIL = GuardianDirectory[selected()]
        LastName.set(LASTNAME)
        FirstName.set(FIRSTNAME)
        ContactNumber.set(CONTACTNNUMBER)
        Address.set(ADDRESS)
        Email.set(EMAIL)
    except IndexError:
        print("No contact was selected.")


# clearing fields
def clear_fields():
    LastName.set("")
    FirstName.set("")
    ContactNumber.set("")
    Address.set("")
    Email.set("")
    print("Fields cleared.")


# exiting the programme
def exit():
    root.destroy()
    print("Exited Guardian Directory")


# buttons
Label(root, text='Last Name', font='arial 12 bold', bg='white').place(x=30, y=25)
Entry(root, textvariable=LastName).place(x=130, y=20)

Label(root, text='First Name', font='arial 12 bold', bg='white').place(x=30, y=75)
Entry(root, textvariable=FirstName).place(x=130, y=70)

Label(root, text='Contact Number', font='arial 12 bold', bg='white').place(x=30, y=125)
Entry(root, textvariable=ContactNumber).place(x=130, y=120)

Label(root, text='Address', font='arial 12 bold', bg='white').place(x=30, y=175)
Entry(root, textvariable=Address).place(x=130, y=170)

Label(root, text='Email', font='arial 12 bold', bg='white').place(x=30, y=225)
Entry(root, textvariable=Email).place(x=130, y=220)

Button(root, text='Add Contact', font='arial 12 bold', bg='white', command=add).place(x=70, y=260)
Button(root, text='Delete Contact', font='arial 12 bold', bg='white', command=delete).place(x=200, y=260)
Button(root, text='Search Contact', font='arial 12 bold', bg='white', command=search).place(x=70, y=300)
Button(root, text='Sort Contacts', font='arial 12 bold', bg='white', command=sorting).place(x=200, y=300)
Button(root, text='View Contact', font='arial 12 bold', bg='white', command=view).place(x=70, y=340)
Button(root, text='Clear', font='arial 12 bold', bg='white', command=clear_fields).place(x=200, y=340)
Button(root, text='Exit', font='arial 12 bold', bg='red', command=exit).place(x=420, y=340)


root.mainloop()

#---code ends here---