import streamlit as st


col1, col2, col3 = st.columns(3)
col1.metric("Name", "Rick Jon")
col2.metric("Age", "34")
col3.metric("Gender", "Male")

col1, col2, col3 = st.columns(3)
col1.metric("Occupation", "Data Science")
col2.metric("Age", "34")
col3.metric("Gender", "Male")