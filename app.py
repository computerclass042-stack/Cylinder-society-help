import streamlit as st
import pandas as pd
import random
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# App Setup
st.set_page_config(page_title="Society Gas Help", page_icon="🧯")

# Google Sheet Connection
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🧯 Society Gas Cylinder System")

# Sidebar for Navigation
menu = ["Customer Booking", "Admin Dashboard"]
choice = st.sidebar.selectbox("Go to", menu)

if choice == "Customer Booking":
    st.header("📋 New Cylinder Booking")
    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    address = st.text_area("Delivery Address")
    qty = st.number_input("Quantity", min_value=1, step=1)
    
    if st.button("Generate OTP & Book"):
        if name and phone:
            otp = random.randint(1000, 9999)
            total_bill = qty * 900
            date_now = datetime.now().strftime("%d-%m-%Y %H:%M")
            
            # Excel ke liye data
            new_data = pd.DataFrame([{
                "Name": name, "Phone": phone, "Address": address, 
                "Quantity": qty, "Amount": total_bill, "OTP": otp, "Date": date_now
            }])
            
            # Sheet Update Logic
            try:
                # Purana data read karo aur naya add karo
                existing_df = conn.read()
                updated_df = pd.concat([existing_df, new_data], ignore_index=True)
                conn.update(data=updated_df)
                
                st.success(f"Booking Successful! Details Vishal ki Excel sheet mein bhej di gayi hain. ✅")
                st.warning(f"YOUR SECRET OTP: {otp}")
                st.info(f"Total Bill: ₹{total_bill}")
            except Exception as e:
                st.error("Excel connection error! Please check Streamlit Secrets.")
        else:
            st.error("Please enter Name and Phone number.")

elif choice == "Admin Dashboard":
    pwd = st.text_input("Admin Password", type="password")
    if pwd == "1234":
        st.subheader("📊 All Society Bookings (Live from Excel)")
        try:
            df = conn.read()
            st.dataframe(df)
        except:
            st.info("No bookings found yet.")
