import random
import csv
from datetime import datetime, timedelta

price_per_cylinder = 900
total_stock = 100
total_sales = 0
admin_password = "1234"

while True:
    print("\n====== Gas Cylinder System ======")
    print("1. Customer Booking")
    print("2. Admin Login")
    print("3. Exit")

    main_choice = input("Enter your choice: ")

    # ================= CUSTOMER PANEL =================
    if main_choice == "1":

        if total_stock <= 0:
            print("Sorry! No Stock Available.")
            continue

        print("\n--- Customer Booking ---")

        name = input("Enter Customer Name: ")
        address = input("Enter Address: ")
        phone = input("Enter Phone Number: ")
        quantity = int(input("Enter Quantity: "))

        if quantity > total_stock:
            print("Not enough stock available!")
            continue

        booking_date = datetime.now()
        delivery_date = booking_date + timedelta(days=3)

        total_amount = quantity * price_per_cylinder
        otp = random.randint(1000, 9999)

        total_stock -= quantity
        total_sales += total_amount

        with open("bookings.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                name,
                address,
                phone,
                quantity,
                delivery_date.strftime("%d-%m-%Y"),
                total_amount,
                otp
            ])

        print("\n✅ Booking Successful!")
        print("Delivery Date:", delivery_date.strftime("%d-%m-%Y"))
        print("Total Bill: ₹", total_amount)
        print("OTP sent to customer:", otp)

        print("\n--- Delivery Verification ---")
        entered_otp = int(input("Delivery Boy Enter OTP(Entre OTP WHEN DELIVERY IS DONE): "))

        if entered_otp == otp:
            print("Delivery Confirmed ✅")
        else:
            print("Invalid OTP ❌ Delivery Failed")

    # ================= ADMIN PANEL =================
    elif main_choice == "2":
        password = input("Enter Admin Password: ")

        if password == admin_password:

            while True:
                print("\n--- Admin Panel ---")
                print("1. Show Stock")
                print("2. Show Total Sales")
                print("3. Back")

                admin_choice = input("Enter choice: ")

                if admin_choice == "1":
                    print("Available Stock:", total_stock)

                elif admin_choice == "2":
                    print("Total Sales: ₹", total_sales)

                elif admin_choice == "3":
                    break

                else:
                    print("Invalid Choice")

        else:
            print("Wrong Password ❌")

    elif main_choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
