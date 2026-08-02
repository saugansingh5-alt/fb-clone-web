total = 0

while True:
    print("\n====== SHOPPING BILLING SYSTEM ======")
    print("1. Rice      - ₹60/kg")
    print("2. Sugar     - ₹45/kg")
    print("3. Milk      - ₹30")
    print("4. Bread     - ₹40")
    print("5. Biscuit   - ₹20")
    print("6. View Bill")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        qty = int(input("Enter Quantity (kg): "))
        total += qty * 60
        print("Rice Added Successfully!")

    elif choice == "2":
        qty = int(input("Enter Quantity (kg): "))
        total += qty * 45
        print("Sugar Added Successfully!")

    elif choice == "3":
        qty = int(input("Enter Quantity: "))
        total += qty * 30
        print("Milk Added Successfully!")

    elif choice == "4":
        qty = int(input("Enter Quantity: "))
        total += qty * 40
        print("Bread Added Successfully!")

    elif choice == "5":
        qty = int(input("Enter Quantity: "))
        total += qty * 20
        print("Biscuit Added Successfully!")

    elif choice == "6":
        print("\n========== SHOPPING BILL ==========")
        print("Total Amount : ₹", total)

        if total >= 1000:
            discount = total * 0.10
            final_bill = total - discount
            print("Discount (10%): ₹", discount)
            print("Final Bill    : ₹", final_bill)
        else:
            print("Discount      : ₹0")
            print("Final Bill    : ₹", total)

    elif choice == "7":
        print("\nThank You for Shopping!")
        break

    else:
        print("Invalid Choice! Please Try Again.")