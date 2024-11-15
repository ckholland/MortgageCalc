import streamlit as st

st.markdown("# Mortgage Calculator")

st.markdown("## Enter Details")

def mortgage_calculator(loan_amount, interest_rate, loan_term, annual_property_tax, annual_home_insurance, pmi_rate=0.005, down_payment=0):

    # Calculate monthly interest rate
    monthly_rate = interest_rate / 12

    # Calculate number of monthly payments
    num_payments = loan_term * 12

    # Calculate loan amount after down payment
    loan_amount -= down_payment

    # Calculate monthly principal and interest payment
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)

    # Calculate monthly property tax and home insurance
    monthly_tax = annual_property_tax / 12
    monthly_insurance = annual_home_insurance / 12

    # Calculate monthly PMI if applicable
    if down_payment / loan_amount < 0.2:
        monthly_pmi = loan_amount * (pmi_rate / 12)
    else:
        monthly_pmi = 0

    # Calculate total monthly payment
    total_monthly_payment = monthly_payment + monthly_tax + monthly_insurance + monthly_pmi

    return total_monthly_payment



loan_amount = st.number_input("Enter loan amount:", value = 300000)
interest_rate = st.number_input("Enter rate:", value = .0415)
loan_term = st.number_input("Term:", value = 30)
annual_property_tax=0
annual_home_insurance=0
pmi_rate=0
down_payment=0

payment = mortgage_calculator(loan_amount,interest_rate,loan_term, annual_property_tax, annual_home_insurance, pmi_rate, down_payment)
