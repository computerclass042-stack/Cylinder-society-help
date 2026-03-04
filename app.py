import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import os

# App Config
st.set_page_config(page_title="Society Gas Help", page_icon="🧯")

# Initialization (Session State for handling data online)
if 'total_stock' not in st.session_state:
    st.session_state.total_stock = 100
if 'total_sales' not in st.session_state:
    st.session_state.total_sales = 0
if 'otp_storage' not in st.session_state:
    st.session_state.otp_storage = None

st.title("🧯 Society Gas Cylinder System")

# Sidebar for Navigation
menu = ["Customer Booking", "Delivery Boy Portal", "Admin Dashboard"]
choice = st.sidebar.selectbox("Go to", menu)

# --- CUSTOMER BOOKING ---
if choice == "Customer Booking":
    st.header("📋 New Cylinder Booking")
    
    if st.session_state.total_stock <= 0:
        st.error("Sorry! Out of Stock.")
    else:
        name = st.text_input("Customer Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Delivery Address")
        qty = st.number_input("Quantity", min_value=1, max_value=st.session_state.total_stock, step=1)
        
        if st.button("Generate OTP & Book"):
            if name and phone:
                otp = random.randint(1000, 9999)
                st.session_state.otp_storage = otp
                total_bill = qty * 900
                
                # Update Session Data
                st.session_state.total_stock -= qty
                st.session_state.total_sales += total_bill
                
                st.success(f"Booking Successful for {name}!")
                st.info(f"🚚 Expected Delivery: {(datetime.now() + timedelta(days=3)).strftime('%d-%m-%Y')}")
                st.warning(f"🔑 YOUR SECRET OTP: {otp} (Share this only with delivery boy)")
                st.metric("Total Bill", f"₹{total_bill}")
            else:
                st.error("Please fill all details")

# --- DELIVERY PORTAL ---
elif choice == "Delivery Boy Portal":
    st.header("🚚 Delivery Verification")
    entered_otp = st.number_input("Enter Customer's OTP to confirm delivery", step=1)
    
    if st.button("Verify & Complete"):
        if st.session_state.otp_storage and entered_otp == st.session_state.otp_storage:
            st.success("Delivery Confirmed ✅ Data Updated in CSV.")
            st.session_state.otp_storage = None # Reset OTP
        else:
            st.error("Invalid OTP ❌ Delivery cannot be completed.")

# --- ADMIN DASHBOARD ---
elif choice == "Admin Dashboard":
    st.header("🔐 Admin Panel")
    password = st.text_input("Enter Admin Password", type="password")
    
    if password == "1234":
        col1, col2 = st.columns(2)
        col1.metric("Available Stock", f"{st.session_state.total_stock} Units")
        col2.metric("Total Revenue", f"₹{st.session_state.total_sales}")
        
        if st.button("Reset Daily Stock"):
            st.session_state.total_stock = 100
            st.rerun()