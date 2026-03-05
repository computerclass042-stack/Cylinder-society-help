import streamlit as st
from datetime import datetime, timedelta
import random

price_per_cylinder = 900

st.title("🧯 Society Gas Cylinder System")
st.subheader("📋 New Cylinder Booking")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
address = st.text_area("Delivery Address")
quantity = st.number_input("Quantity", min_value=1, step=1)

if st.button("Generate OTP & Book"):

    booking_date = datetime.now()
    delivery_date = booking_date + timedelta(days=3)

    total_amount = quantity * price_per_cylinder
    otp = random.randint(1000,9999)

    st.success("Booking Successful ✅")

    st.write("Delivery Date:", delivery_date.strftime("%d-%m-%Y"))
    st.write("Total Bill: ₹", total_amount)
    st.write("OTP:", otp)

