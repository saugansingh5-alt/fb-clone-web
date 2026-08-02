contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email
        }

        contacts.append(contact)
        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found.")
        else:
            print("\n===== CONTACT LIST =====")
            for i, contact in enumerate(contacts, start=1):
                print(f"\nContact {i}")
                print("Name  :", contact["Name"])
                print("Phone :", contact["Phone"])
                print("Email :", contact["Email"])

    elif choice == "3":
        name = input("Enter Name to Search: ")
        found = False

        for contact in contacts:
            if contact["Name"].lower() == name.lower():
                print("\nContact Found")
                print("Name  :", contact["Name"])
                print("Phone :", contact["Phone"])
                print("Email :", contact["Email"])
                found = True
                break

        if not found:
            print("Contact Not Found.")

    elif choice == "4":
        name = input("Enter Name to Delete: ")
        found = False

        for contact in contacts:
            if contact["Name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found.")

    elif choice == "5":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")