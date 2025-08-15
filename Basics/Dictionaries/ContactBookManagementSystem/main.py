
print("Welcome to contact management system")
contact = {}


while(True):
    choice = int(input("what do you want to do?: \n1. Add contact, \n2. Find Contact, \n3. Delete Contact, \n4. To view all Contacts: \n5. Exit"))
    if(choice==1):
        # add contact 
        choice1 = input("Do you want to add contact(y/n): ")
        if(choice1=="y"):
            phoneNumber = int(input("Enter Phone Number: "))
            contactName = input("Enter name: ")

            

            contact[phoneNumber] = {"Phone Number":phoneNumber, "Name":contactName}
            print(contact.get(phoneNumber),"has been added")
        else:
            print("No contact added")

        #find contact
    elif(choice==2):
        choice2 = int(input("Enter the Ph. number of the contact you want to find: "))
        print(contact.get(choice2))

    # delete contact
    elif(choice==3):
        choice3 = int(input("Enter the Ph. number of the contact you want to find: "))
        poppedContact = contact.pop(choice3, "Not found")
        print(poppedContact)

    elif(choice==4):
        for c in contact.values():
            print(c)

    elif(choice==5):
        print("Exiting . . .")
        break
    #exit
    else:
        print("\nEnter valid input\n")

    

    