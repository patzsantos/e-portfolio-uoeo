# Guardian Directory

The Guardian Directory (GD) is a phonebook programme intended for the record-keeping of the information of parents and guardians of students in Early Learning Centres (ELC) such as daycares and nurseries.

The parental and guardian records kept in the GD are especially helpful in the event that correspondence with them is necessary. An example of this is, when there are any school announcements, or if teachers need to communicate with the parents or guardians, all they have to do is search for their contact information from the Guardian Directory. They can quickly reach out to them by phone, and if not, through e-mail. The address is there in case any mail, such as invitations to school events, are needed to be sent out by the ELCs.

### Running the code
 This code was written on **PyCharm** and runs on **Python 3.11**. 

If you are having trouble running the code in Codio, please run it on PyCharm. 
The preview of the GUI, which was imported from **Tkinter** can also be previewed in PyCharm.

Some changes to running the program has been modified and improved from the data structure and algorithm design proposal based on Assignment 1. 

### Functions of the Guardian Directory

#####
**The Guardian Directory has 7 functions:**
1) Add contact
2) Delete contact
3) Search contact
4) Sort contact 
5) View contact
6) Clear fields
7) Exit

In the fields, the contact information details can be viewed. The details that will be asked upon listing a contact are: 
1) Last name
2) First name
3) Contact Number
4) Address
5) E-mail

#### > Add Contact
####
![AddContact](https://raw.githubusercontent.com/patzsantos/GuardianDirectory/main/GD_Screenshots/AddContact.gif)
####
If you want to add a parent or guardian to the directory, just fill in the fields with contact *Last Name, First Name, Contact Number, Address, and E-mail.* Once done, click **Add Contact**.

####
####

#### > Delete Contact
####
![DeleteContact](https://raw.githubusercontent.com/patzsantos/GuardianDirectory/main/GD_Screenshots/DeleteContact.gif)
### 
If you want to delete a contact, select the contact you want to delete from the list, and click **Delete Contact**. 

There are other alternatives to deleting a contact. 
First is by typing in the contact **Last Name** in the field, then clicking **Search Contact**, after which you can select **Delete Contact**. 
The second alternative is typing in the contact **Last Name** in the field, then clicking **View Contact** before selecting **Delete Contact**. 

These, however, are adviseable only when there are many contacts stored in the GD, which makes finding them difficult. 

Here, we can find the first difference from Assignment 1, where First Name was required to be written in the field. This decision to change to last name was made since it is safe to assume that the ELC employees would find it easier to look for the family name of the student in the GD. 

This change would continue to be applied in the next functions, which are **Search Contact** and **Sort Contacts**.

####
####

#### > Search Contact

![SearchContact](https://raw.githubusercontent.com/patzsantos/GuardianDirectory/main/GD_Screenshots/SearchContact.gif)
####
If you want to search for contact information, type in the *Last Name* and click **Search Contact**. The rest of their details will then be displayed. 


#### > Sort Contacts

![SortContact](https://raw.githubusercontent.com/patzsantos/GuardianDirectory/main/GD_Screenshots/SortContacts.gif)
####
When you click **Sort Contacts**, the directory will list the *Last Names* in descending order. 

This is the second difference from Assignment 1, where the intial proposal was to just arrange the first names alphabetically with the sort function. 


#### > View Contact and Clear Fields

![ViewandClear](https://raw.githubusercontent.com/patzsantos/GuardianDirectory/main/GD_Screenshots/ViewandClear.gif)
####
If you want to view a contact and their details, click **View Contact**. 
If you want to clear the fields, click **Clear**. 

These two additional functions were proposed and added by [michael305y](https://github.com/michael305y), who helped me, through [discuss.python.org](discuss.python.org), how to make the **Search Contact** and **Sort Contacts** functions work. 


#### > Exit the programme

Click the **Exit** button to close the programme. 

### Testing the Code
Manual Testing was used to test the code. This changed from the supposed unittest that was proposed in Assignment 1. The code run successfully. The GUI displays and operates the correct buttons when the programme is opened, and the programme can be closed when the exit button is selected. 
The programme is also able to function successfully, as it can add, delete, search, sort, view, and clear contacts. 
![Test](https://raw.githubusercontent.com/patzsantos/GuardianDirectory/main/GD_Screenshots/unittest.png) 

### How to Better Improve the Code
As mentioned in Assignment 1, completing the U function, which stands for Update, in the CRUD method, is one way to further improve the functionality of the Guardian Directory. 

Another thing to look into is the security of the data privacy of the guardians stored in the GD. 

*What software should be used in order to strengthen the cyber security of the GD?* 
###
*How long should the contacts be stored in the directory?*

These are questions to ask in the future, when further developing the programme. 

### Purpose 

This code was built as a requirement in the Launching Into Computer Science Module of University of Essex Online, and serves as the Assignment Part 2 project of the course. 

### Credits

As I mentioned earlier, a big shoutout to [michael305y](https://github.com/michael305y), who helped a great deal in not just kindly pointing out my mistakes, but also in teaching me how to make my code actually work the way I want it to. 

The GUI of the Guardian Directory was inspired by the tutorials of [Sam CodeHub](https://www.youtube.com/watch?v=oBVzKHsA4J8&list=WL&index=1&t=78s) and [Geekedu](https://www.geekedu.org/blogs/python-game-for-kids-tkinter-address-book). 

The gifs of how the function work, as seen above, were converted on [cloudconvert](https://cloudconvert.com/).

