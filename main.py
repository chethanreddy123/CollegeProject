import streamlit as st

st.title("Currency Converter")

Type = st.radio(
    "What Type of Conversion you want to make:",
    ('Indian Rupees to US Dollor', 'US Dollor to Indian Rupees'))

if Type == 'Indian Rupees to US Dollor':
    amount = float(st.text_input("Enter the Indian Rupees" , 0))
    dollor = round(amount / 82.27 , 2)
    st.caption("The amount in India Ruppes is %s dollor "%dollor)
else:
    pass
