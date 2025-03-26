import streamlit as st
import pandas as pd
import numpy as np
import joblib
# Title of the app
st.title("🚚 Delivery Time Prediction App")
# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Upload Data"])
if page == "Home":
    # Header
    st.header("📦 Enter Order Details")
    # Input fields for order details
    product_category = st.selectbox(
        "Select Product Category",
        ["Electronics", "Clothing", "Books", "Furniture", "Toys", "Groceries"]
    )
    customer_location = st.text_input("Enter Customer Location (City, State)")
    shipping_method = st.selectbox(
        "Select Shipping Method",
        ["Standard", "Express", "Overnight"]
    )
    order_weight = st.number_input("Enter Order Weight (kg)", min_value=0.1, step=0.1)
    distance = st.number_input("Enter Distance to Customer (km)", min_value=1, step=1)
    # Validate inputs
    if not customer_location:
        st.warning("⚠️ Please enter a valid customer location.")
    else:
        # Predict button
        if st.button("Predict"):
            # Placeholder for ML model prediction
            # Replace this with your trained model's prediction logic
            # Example: prediction = model.predict([[product_category, shipping_method, order_weight, distance]])
            prediction = np.random.randint(1, 10)  # Random delivery time between 1 and 10 days

            # Display the result
            st.success(f"🚀 Expected delivery time: {prediction} days")

            # Additional details
            st.info("Note: This is a placeholder prediction.")

elif page == "Upload Data":
    # Upload data page
    st.header("📤 Upload Historical Data")
    uploaded_file = st.file_uploader("Upload a CSV file with historical order data", type=["csv"])

    if uploaded_file:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)
        st.write("📊 Preview of Uploaded Data:")
        st.dataframe(data.head())

        # Placeholder for training a model
        st.info("You can use this data to train a machine learning model.")

elif page == "About":
    # About page
    st.header("ℹ️ About This App")
    st.write("""
        This application predicts the expected delivery time for an order based on the following details:
        - Product Category
        - Customer Location
        - Shipping Method
        - Order Weight
        - Distance to Customer

        **How It Works:**
        - The app uses a machine learning model (or placeholder logic) to estimate delivery time.
        - You can upload historical data to train your own model.

        **Technologies Used:**
        - Python
        - Streamlit
        - Machine Learning (optional)
    """)

    st.write("Developed by tejas.")

# Footer
st.sidebar.info("Powered by Streamlit")
